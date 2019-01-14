from datetime import datetime 
import pandas as pd
import sys

#print(str(datetime.now()))
yy= str (str(datetime.now().year))
filename ='out.2018-09-01.Saturday.23.06.27.txt.gz'
#filename = sys.argv[1]

dic= {  'jan' : '01',
        'feb' : '02',
        'mar' : '03',
        'apr' : '04',
        'may' : '05',
        'jun' : '06',
        'jul' : '07',
        'aug' : '08',
        'sep' : '09', 
        'oct' : '10',
        'nov' : '11',
        'dec' : '12'


}

df =pd.read_csv('C:/Users/aalshobaki/Desktop/deleteme/'+filename, compression = 'gzip', header =None , sep ="\n" , names =["raw"]) 
df =df["raw"].str.extract(r'((?P<Month>\w{3})\s{1,2}(?P<day>\d{1,2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}))+?.*?(?P<ip1>[0-9]+(?:\.[0-9]+){3})/(?P<port1>[0-9]+)+?.*?(?P<ip2>[0-9]+(?:\.[0-9]+){3})/(?P<port2>[0-9]+)+?.*?(?P<ip3>[0-9]+(?:\.[0-9]+){3})/(?P<port3>[0-9]+)+.*?(?P<ip4>[0-9]+(?:\.[0-9]+){3})/(?P<port4>[0-9]+)+' )
df =df.drop([0,'ip4','port4'], axis=1)
df= df.dropna()
df['day'] = df['day'].apply(lambda x: '{0:0>2}'.format(x))
df["Month"] = df["Month"].str.lower().map(dic)
df['start_time'] = yy+'-'+df["Month"]+'-'+df["day"]+' '+df["hour"]+":"+df["minute"]+":"+df["second"]+".000"
df['start_time_int'] = yy+df["Month"]+df["day"]+df["hour"]+df["minute"]+df["second"]
df['SourceID'] = 2
df['SourceFileName'] = filename
df['insertdate'] = str( datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f3')[:-4])
df['dateid'] = yy+df["Month"]+df["day"]

df.to_csv('C:/Users/aalshobaki/Desktop/deleteme'+filename+'.csv',header=False, index=False, sep='^', encoding='utf-8', columns = 	['start_time','ip1','port1','ip2','port2','ip3','port3','insertdate','SourceFileName','SourceID', 'start_time_int','dateid'])
#print(str(datetime.now()))

