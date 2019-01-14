import pyodbc
import pandas
import re
import os

#TableName = 'XXPOS_ADJ_DETAILS'

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
#AND (a.definition) LIKE '%'''

#sql = sql + TableName +'%\'' 

data = pandas.read_sql(sql,cnxn)
data = pandas.read_sql(sql,cnxn)

regex_pat = re.compile("/\*.*?\*/",re.DOTALL )

data["sql"] = data["sp_definition"].str.replace(regex_pat, '',regex=True)

regex_pat = re.compile("--.*?\n" )
data["sql"] = data["sql"].str.replace(regex_pat, '',regex=True)
data["sql"] = data["sql"].str.upper()
data["sql"] = data["sql"].str.replace('[DBO].', '',regex=False)
data["sql"] = data["sql"].str.replace('DBO.', '',regex=False) 
data["sql"] = data["sql"].str.replace('[UMDW_STAGING]', 'UMDW_STAGING',regex=False) 
data["sql"] = data["sql"].str.replace('[BACKOFFICE]', 'BACKOFFICE',regex=False) 
#data["sql"] = data["sql"].str.replace('[', '',regex=False) 
#data["sql"] = data["sql"].str.replace(']', ' ',regex=False) 

data['index1'] = data.index

#df = data["sql"].str.extractall(r'INSERT\s*INTO\s*(?P<To_table>[^#]\S*)\s*.*?select+(?:.*?\s*)from\s*(?P<From_table>[^#(\s]+)',  re.DOTALL | re.IGNORECASE) 
#df = data["sql"].str.extractall(r'(?P<Script>INSERT\s*INTO\s*(?P<To_table>[^#]\S*)\s*.*?select+(?:.*?\s*)from\s*(?P<From_table>[^#(\s]+))',  re.DOTALL | re.IGNORECASE) 
#df = data["sql"].str.extractall(r'(?P<Script>INSERT\s*INTO\s*(?P<To_table>[^#]\S*)\s*.*?select+(?:.*?\s*)from\s*(?P<From_table>[^#(\s]+).{1,600})',  re.DOTALL | re.IGNORECASE) 
df = data["sql"].str.extractall(r'(?P<Script>INSERT\s*INTO\s*(?P<To_table>[^#]\S*)\s*.*?select+(?:.*?\s*)from\s*(?P<From_table>\S*).{,200})',  re.DOTALL | re.IGNORECASE) 

df = df.reset_index()
new_df = pandas.merge(df, data,  how='right', left_on=['level_0'], right_on = ['index1'])
new_df=new_df.dropna()

#re.findall(r'INSERT\s*into\s*(\S*)\s*.*?select+(?:.*?)from\s*(\S*)', data["sql"][6] ,  re.DOTALL | re.IGNORECASE)
summary = new_df[['sp_name','From_table','To_table', 'Script']].drop_duplicates() 

summary.loc[summary['From_table'].str.contains("XXPOS_DELETED_LOAN".upper()),['Script', 'From_table']]
summary.loc[summary['From_table'].str.contains("XXPOS_DELETED_LOAN".upper()),['Script']]

print(summary["Script"][650])

summary[summary['From_table'].str.contains("XXPOS_DELETED_LOAN".upper())] 
print(summary["Script"][183])

#######################------------------
m=regex.search(r"\s(?:JOIN|FROM|APPLY)[\s/[]+(?P<from_table>[^#(\s]+).*,[\s]*(?P<from_table>[\S]*)?", data["withoutcomments"][0])
