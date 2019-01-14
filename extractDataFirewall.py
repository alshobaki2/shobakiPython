from datetime import datetime 
import pandas as pd
import sys
from os.path import isfile, join
from os import listdir
import os, fnmatch
import subprocess


path = path = 'D:/Firewall/Sources/Firewall/'
#filename = 'firewall.gz'
pattern = "*w*.gz" 
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))& fnmatch.fnmatch(f, pattern) ]


for fn in onlyfiles:

    firewall =pd.read_csv(path+fn,chunksize =10000000, compression = 'gzip', index_col=False , header =None ,  sep=' '  , engine='c' , usecols=[0,1,2,3,6,9,10,11,13,14], parse_dates =  {'start_time' : [0, 1,2,3]} , infer_datetime_format = True, skip_blank_lines  = True  , low_memory = False, names  = [0,1,2,3, 'SOURCE_IP','PUBLIC_IP','BEFORE_NAT_PORT','AFTER_NAT_PORT', 'DESTINATION_IP', 'DESTINATION_PORT'] )
    i = 0
    for chunk in firewall:
        i = i+1
        chunk['dateid']=chunk['start_time'].dt.strftime('%Y%m%d')
        chunk['start_time_int']=chunk['start_time'].dt.strftime('%Y%m%d%H%M%S')
        chunk['insertdate'] = str( datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f3')[:-4])
        chunk['SourceID'] = 1
        chunk['SourceFileName'] = fn
        chunk.to_csv(path+"new_file_" + fn+str(i)+".txt",header=False, index=False, sep='^', encoding='utf-8', mode ='a', columns = ['start_time','PUBLIC_IP','SOURCE_IP','DESTINATION_IP','BEFORE_NAT_PORT','AFTER_NAT_PORT','DESTINATION_PORT','insertdate' ,'SourceFileName','SourceID', 'start_time_int','dateid'] )


args = 'dwloader.exe -U ETL_USER -P pass@word1 -S 192.168.40.50  -T firewall.dbo.Firewall_Fact_201809_test -i D:/Firewall/Sources/Firewall/*.txt -M fastappend -r 0x0d0x0a  -t "^" -e UTF8 -rv 1000 -rt value -R D:/Firewall/Sources/Firewall/FileName.bad -E -m '
subprocess.call(args,shell=True)