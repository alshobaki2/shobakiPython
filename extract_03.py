from datetime import datetime 
import pandas as pd
import sys

print(str(datetime.now()))
yy= str (str(datetime.now().year))
filename ='out.2018-09-17.Monday.09.36.27.txt.gz'

df2 =pd.read_csv('C:/Users/aalshobaki/Desktop/'+filename, compression = 'gzip', header =None , sep ="\n" , names =["raw"]) 

df5 =df2["raw"].str.extract(r'(?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})' )

df6 = df2["raw"].str.extractall(r'(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+)' )

del df2

df6 =df6.unstack()
df6.columns= ["ip1","ip2","ip3","ip4","port1","port2","port3","port4"]
df6=df6.join(df5)

df6.to_csv('C:/Users/aalshobaki/Desktop/'+filename+'.csv',header=False, index=False, sep='^', encoding='utf-8')
print(str(datetime.now()))



###############
print(str(datetime.now()))
df66 = df2["raw"].str.extract(r'(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+).*(?P<ip2>[0-9]+(?:\.[0-9]+){3})/(?P<port2>[0-9]+).*(?P<ip3>[0-9]+(?:\.[0-9]+){3})/(?P<port3>[0-9]+)' )
print(str(datetime.now()))


print(str(datetime.now()))
df66 = df2["raw"].str.extractall(r'(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+).{3}' )
print(str(datetime.now()))




print(str(datetime.now()))
df66 = df2["raw"].str.extract(r'((?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}))+?(.*?((?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+))){3}' )
print(str(datetime.now()))




print(str(datetime.now()))
df66 = df2["raw"].str.extract(r'((?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}))+?.*?(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+)+?.*?(?P<ip2>[0-9]+(?:\.[0-9]+){3})/(?P<port2>[0-9]+)+?' )
print(str(datetime.now



print(str(datetime.now()))
df66 = df2["raw"].str.extract(r'((?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}))+?.*?(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+)+?.*?(?P<ip2>[0-9]+(?:\.[0-9]+){3})/(?P<port2>[0-9]+)+?.*?(?P<ip3>[0-9]+(?:\.[0-9]+){3})/(?P<port3>[0-9]+)+?' )
print(str(datetime.now()))




print(str(datetime.now()))
df66 = df2["raw"].str.extract(r'((?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}))+?.*?(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+)+?.*?(?P<ip2>[0-9]+(?:\.[0-9]+){3})/(?P<port2>[0-9]+)+?.*?(?P<ip3>[0-9]+(?:\.[0-9]+){3})/(?P<port3>[0-9]+)+.*?(?P<ip4>[0-9]+(?:\.[0-9]+){3})/(?P<port4>[0-9]+)+' )
print(str(datetime.now()))