import pyodbc
import pandas
import re
import os

#TableName = 'XXPOS_ADJ_DETAILS'
def removeComments(x):
    c1= x.find("--")
    c2= x.find("/*")
    if (c1 == -1) & (c2 == -1):
        return x
    elif (c1 == -1) & (c2 > -1):
        to = x.find("*/",c2)
        if to >-1:
            return removeComments(x[0:c2]+x[to+2:])
        else:
            return removeComments(x[0:c2])
    
    elif (c2 == -1) & (c1 > -1):
        to = x.find("\n",c1)
        if to >-1:
            return removeComments(x[0:c1]+x[to:])
        else:
            return removeComments(x[0:c1])        

    elif (c2 > c1 ):
        to = x.find("\n",c1)
        if to >-1:
            return removeComments(x[0:c1]+x[to:])
        else:
            return removeComments(x[0:c1])
    else:
        to = x.find("*/",c2)
        if to >-1:
            return removeComments(x[0:c2]+x[to+2:])
        else:
            return removeComments(x[0:c2]) 

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=192.168.40.50,17001;"
                      "Database=UMDW;"
                      "UID=ETL_USER;"
                      "PWD=pass@word1;"
                      )
cursor = cnxn.cursor()

sql = '''
SELECT OBJECT_NAME(a.object_id) sp_name,       (a.definition) sp_definition FROM sys.sql_modules a WHERE
OBJECTPROPERTY(object_id, 'IsProcedure') = 1  
'''


data = pandas.read_sql(sql,cnxn)



data["sp_definition"] = data["sp_definition"].apply(removeComments)
data["sp_definition"] = data["sp_definition"].str.replace('[', '',regex=False) 
data["sp_definition"] = data["sp_definition"].str.replace(']', '',regex=False) 
data["sp_definition"] = data["sp_definition"].str.replace(')', ') ',regex=False) 
data["sp_definition"] = data["sp_definition"].str.upper()
data['index1'] = data.index
df=data["sp_definition"].str.extractall(r'\s+(from|into|update|join|table|APPLY)[\s|(]+(\S*)',  re.DOTALL | re.IGNORECASE) 
df = df.reset_index()
new_df = pandas.merge(df, data,  how='right', left_on=['level_0'], right_on = ['index1'])
new_df=new_df.dropna()
del new_df["sp_definition"]
del new_df["match"]
del new_df["level_0"]
del new_df["index1"]
new_df.columns = ['keyword','Table','Sp']
new_df=new_df[new_df["Table"]!='SELECT']
new_df =new_df[~new_df["Table"].str.contains("#")]
#new_df.to_csv("C:\\Users\\aalshobaki\\Desktop\\tables_used_by_spV2.csv")


cnxn2 =  pyodbc.connect('Driver={SQL Server};''Server=192.168.40.222;''Database=ContinuousLoad;''Trusted_Connection=yes;')
cursor2 = cnxn2.cursor()

sql2 = '''
WITH ItemContentBinaries AS 
( 
  SELECT 
     ItemID
    ,CASE WHEN ParentID IS NOT NULL THEN Name ELSE 'Home' END AS Name
    ,CASE WHEN ParentID IS NOT NULL THEN [Path] ELSE '/' END AS [Path]
    ,ParentID
    ,[Type] 
    ,CASE Type 
      WHEN 1 THEN 'Folder'
      WHEN 2 THEN 'Report' 
      WHEN 3 THEN 'Resource'
      WHEN 4 THEN 'Linked Report'
      WHEN 5 THEN 'Data Source' 
      WHEN 6 THEN 'Report Model'
      WHEN 7 THEN 'Report Part'
      WHEN 8 THEN 'Shared Dataset' 
      ELSE 'Other' 
     END AS TypeDescription 
    ,CONVERT(varbinary(max),Content) AS Content    
  FROM ReportServer.dbo.Catalog 
   WHERE Type IN (2,5,7,8, 5)  --You could limit the query to return only certain types here....
), 
-- The second CTE strips off the BOM if it exists from the 
-- beginning of the XML.  
ItemContentNoBOM AS 
( 
  SELECT 
     ItemID
    ,Name
    ,[Path]
    ,ParentID
    ,[Type] 
    ,TypeDescription 
    ,CASE 
      WHEN LEFT(Content,3) = 0xEFBBBF 
        THEN CONVERT(varbinary(max),SUBSTRING(Content,4,LEN(Content))) 
      ELSE 
        Content 
    END AS Content 
  FROM ItemContentBinaries 
),
--This CTE strips off the trailing 0x00 if there is one
ItemContentNoNullTerm AS
(
  SELECT 
     ItemID
    ,Name
    ,[Path]
    ,ParentID
    ,[Type] 
    ,TypeDescription 
    ,CASE 
      WHEN RIGHT(Content,1) = 0x00 
        THEN CONVERT(varbinary(max),LEFT(Content,LEN(Content)-1)) 
      ELSE 
        Content 
    END AS Content 
  FROM ItemContentNoBOM 
),
--This CTE gets the content in its varbinary, varchar and xml representations... 
CatalogContentView AS
(
SELECT 
   ItemID
  ,Name
  ,[Path]
  ,ParentID
  ,[Type] 
  ,TypeDescription 
  ,Content                                           --varbinary 
  , CONVERT(varchar(max),(Content)) AS ContentVarchar   --varchar 
  ,CONVERT(xml,Content) AS ContentXML                --xml 
FROM ItemContentNoNullTerm)



select *, 
(SUBSTRING(ContentVarchar, patindex( '%<CommandText>%',ContentVarchar) + 13, patindex( '%</CommandText>%',ContentVarchar)-patindex( '%<CommandText>%',ContentVarchar) )) as query,
SUBSTRING(ContentVarchar, patindex( '%<CommandType>%',ContentVarchar) +13, patindex( '%</CommandType>%',ContentVarchar) -patindex( '%<CommandType>%',ContentVarchar) ) as CommandType

from CatalogContentView -- where name like '%waive%'
'''


data2 = pandas.read_sql(sql2,cnxn2)