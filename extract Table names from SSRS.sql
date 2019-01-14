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
dbo.RemoveComments (SUBSTRING(ContentVarchar, patindex( '%<CommandText>%',ContentVarchar) + 13, patindex( '%</CommandText>%',ContentVarchar)-patindex( '%<CommandText>%',ContentVarchar) )) as query,
SUBSTRING(ContentVarchar, patindex( '%<CommandType>%',ContentVarchar) +13, patindex( '%</CommandType>%',ContentVarchar) -patindex( '%<CommandType>%',ContentVarchar) ) as CommandType

from CatalogContentView -- where name like '%waive%'

