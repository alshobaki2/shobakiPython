
# coding: utf-8

# In[243]:


import re
import datetime 
import gzip
import pandas as pd
import sys


# In[248]:


filename ='out.2018-09-17.Monday.09.36.27.txt.gz'


# In[249]:


df2 =pd.read_csv('C:/Users/aalshobaki/Desktop/'+filename, compression = 'gzip', header =None , sep ="\n" , names =["raw"]) 


# In[250]:


df5 =df2["raw"].str.extract(r'(?P<Month>\w{3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})' )


# In[251]:


df6 = df2["raw"].str.extractall(r'(?P<ip>[0-9]+(?:\.[0-9]+){3})/(?P<port>[0-9]+)' )


# In[252]:


del df2


# In[255]:


df6 =df6.unstack()


# In[256]:


df6=df6.join(df5)


# In[257]:


df6

