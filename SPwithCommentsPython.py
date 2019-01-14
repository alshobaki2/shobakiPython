import pyodbc
import pandas
import re


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=192.168.40.50,17001;"
                      "Database=UMDW;"
                      "UID=ETL_USER;"
                      "PWD=pass@word1;"
                      )
cursor = cnxn.cursor()

sql = "SELECT OBJECT_NAME(a.object_id) sp_name,       (a.definition) sp_definition FROM sys.sql_modules a WHERE OBJECTPROPERTY(object_id, 'IsProcedure') = 1"
data = pandas.read_sql(sql,cnxn)

regex_pat = re.compile("/\*.*?\*/",re.DOTALL )

data["withoutcomments"] = data["sp_definition"].str.replace(regex_pat, '',regex=True)

regex_pat = re.compile("--.*?\n" )

data["withoutcomments"] = data["withoutcomments"].str.replace(regex_pat, '',regex=True)



df=data["withoutcomments"].str.extractall(r'into[\s/[]+(?P<into_table>[^#][^(\s]+)' , re.IGNORECASE) 

df = df.reset_index()

data['index1'] = data.index

new_df = pandas.merge(df, data,  how='right', left_on=['level_0'], right_on = ['index1'])
IntoTables = new_df[['sp_name','into_table']]
IntoTables [IntoTables ['sp_name'] == 'alaaTest']





df=data["withoutcomments"].str.extractall(r'into[\s/[]+(?P<into_table>[^#][^(\s]+)' , re.IGNORECASE) 
df=data["withoutcomments"].str.extractall(r'into[\s/[]+(?P<into_table>[^#][^(\s]+)' , re.IGNORECASE) 
df2=data["withoutcomments"].str.extractall(r'\s(?:join|from|apply)[\s/[(]+(?P<from_table>(?!SELECT)[^#)(\s]+)+\s*' , re.IGNORECASE) 
df2=data["withoutcomments"].str.extractall(r'\s(?:join|from|apply)[\s/[(]+([\S]*[\s]*,[\s]*)?(?P<from_table>(?!SELECT)[^#)(\s,]+)+(\s*,?)+' , re.IGNORECASE) 


df2=data["withoutcomments"].str.extractall(r'\s(?:join|from|apply)[\s/[(]+(\S*\s*,\s*)?(?P<from_table>(?!SELECT)[^#)(\s,]+)+' , re.IGNORECASE) 
df2=data["withoutcomments"].str.extractall(r'\s(?:join|from|apply)([^,]*,)*(?P<from_table>(?!SELECT)[^#)(,\s]+)+' , re.IGNORECASE) 