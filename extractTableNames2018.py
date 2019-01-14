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


data = pandas.read_sql(sql,cnxn)
data = pandas.read_sql(sql,cnxn)

data["sp_definition"] = data["sp_definition"].str.replace('[', '',regex=False) 
data["sp_definition"] = data["sp_definition"].str.replace(']', '',regex=False) 
data["sp_definition"] = data["sp_definition"].str.replace(')', ') ',regex=False) 
data["sp_definition"] = data["sp_definition"].str.upper()
data['index1'] = data.index
df=data["sp_definition"].str.extractall(r'(from|into|update|join|table|APPLY)[\s|(]*(\S*)',  re.DOTALL | re.IGNORECASE) 
df = df.reset_index()
df