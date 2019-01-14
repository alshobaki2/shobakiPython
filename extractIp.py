
import re
import datetime 
#import gzip
import pandas as pd
import sys

print(str(datetime.datetime.now()))
yy= str (str(datetime.datetime.now().year))

mylist =[]
print(sys.argv[1] )
filename = sys.argv[1]
#path =
with gzip.open('C:/Users/aalshobaki/Desktop/'+filename, 'r') as f:
    mylist = f.readlines()

newlist= []
for x in mylist:
    Ips= (re.findall( r'([0-9]+(?:\.[0-9]+){3})/([0-9]+)',str(s)))
    sdate =re.findall( r'((\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2}))',str(s) )
    newlist.append(list(sdate[0])+list(Ips[0]) +list(Ips[1]) +list(Ips[2]) )


df =pd.DataFrame(newlist, columns=['sdate','address1','address2','address3','address4'] )
df=df.dropna()

del newlist

df['ip1'] = list(pd.DataFrame(list(df["address1"]))[0])
df['port1'] = list(pd.DataFrame(list(df["address1"]))[1])

df['ip2'] = list(pd.DataFrame(list(df["address2"]))[0])
df['port2'] = list(pd.DataFrame(list(df["address2"]))[1])

df['ip3'] = list(pd.DataFrame(list(df["address3"]))[0])
df['port3'] = list(pd.DataFrame(list(df["address3"]))[1])


df['sdate'] = pd.to_datetime(yy+' '+df['sdate'], format='%Y %b %d %H:%M:%S')
df['dateid'] = df['sdate'].dt.strftime('%Y%m%d')
df['start_time_int'] = df['sdate'].dt.strftime('%Y%m%d%H%M%S')
df['SourceID'] = 2
df['SourceFileName'] = filename
df['insertdate'] = str( datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f3')[:-4])
df.to_csv('C:/Users/aalshobaki/Desktop/'+filename+'.csv',header=False, index=False, sep='^', encoding='utf-8', columns = 	['sdate','ip1','port1','ip2','port2','ip3','port3','insertdate','SourceFileName','SourceID', 'start_time_int','dateid'])
print(str(datetime.datetime.now()))




df5 =df2["full"].str.extract(r'(\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})' )
df6 = df2["full"].str.extractall(r'([0-9]+(?:\.[0-9]+){3})/([0-9]+)' )
df6.unstack(level =-1)[0]+df5



df5 =df2["full"].str.extract(r'(?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})' )
df6 = df2["full"].str.extractall(r'(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+)' )
df6 =df6.unstack()
#df6["Month"],df6["day"] = df5["Month"],df5["day"]
df6=df6.join(df5)
df6.columns= ["ip1","ip2","ip3","ip4","por1","port2","port3","port4"]