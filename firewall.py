Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> path = 'C:/Users/aalshobaki/Desktop/firewall'
>>> fn ='syslogs.gz'
>>> import sys
import re

SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> import sys
>>> import re
>>> import gzip
>>> from datetime import datetime
>>> import io
>>> f = open(path+fn, "rb")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f = open(path+fn, "rb")
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/aalshobaki/Desktop/firewallsyslogs.gz'
>>> path = 'C:/Users/aalshobaki/Desktop/firewall/'
>>> f = open(path+fn, "rb")
>>> f.readline()
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x04\x00\xa4}Y\x92$;\x92\xdc?Ex\x87\xbc\xc0\x84`3,s\t\x9e\x81\xc2\xf9\xe6\x0f\xe7\xfeBS5\x8f\x0c\x98Gf\x06\x80\x92\x9e~=\xddU\xe5\xe5\t\x07\x0c\xb6\xe8\x92B\xec_\xff\xeb\xff\xfc\xf7W\xa8_\xa1\xfcg,\xff\x19\xf2\xd7\xff\xfb\xbf\xff\xfb\xbf\xbf\xeaW\x0c\x8f\x14\xfa#\x86\xf0\x88\xa5|\xfd\xc7\x97<\x8a<b\xd6\xffI\xf2W\xee)\xb4/\xa9Q\xba\xfeR\xec\xf2\xa8\xfa\xfbc}\xc4\xf1UJ\xfe\x9f\xff#\xfd\xfa\xe8\xd8\xbe\x9f\x9d\xda#\xa5\xe9\xd9\xed\xd1\xcbW\x96R\xc6W\x1a\xbdD<\xba%}n{\xe8\xff\xd5\xfa\xe9\xd1\xaf\xb7\x1e\xe9\xa1o\xf9|pI\x8fX\xd3\x97\x04\xd1\xdf)1e\xd1_J1?b\xaf\x8f\x9c\xf1\xd2=,\xbesN\x8f\x1c_O\xd6\xd5\x19\xed\xab\xa4!\xf2\x15S(xr\x19\x0f\x89\xfa;u5D_\xa9\x85\xf0\xe7\xc3\xbf\xdf:a\xad\xdbx=\\\x1f\x92\xf4\x87\x96\xac?z\xcc9\xf4\xe7k\xb7\xa2\x8f\x97GZ\\\x10\xfd:\x8f\xf1zn.\xba\xa4_"\xb9$}l\x0cI\x7fE\xbf`\x92\xc7\x10~\x90\xd5\xc5\xc0\xbb\xa4<\xdcj\xe0\'\x96\x12\xca\xd7\xa8\xa9\xe9\xaf\xe8G\x8d\xa2k\xf6\xa8\xba_\x966Fz\x8c\xf2\x98\xb6\x9c.C\x0f\xfaK\xba\x14Q\xb7\x05\xdeV?\xe1#\x95\xf2\x18\x8f\xf15R\\\xfdv\xfa\xe3\xc5\x96\xe7\xfd\xa6\xebPR\x89E\xf7[\x1e|\xb2\xee\x1c|8}xJ\xf8{\x96\xbe\x9c\xfe!}\xf8\xfc`\xfdo\xb9W\xd1\x8d\x1cG\xb1\xefV\x1f\x82%\xd3\xdf\xaa\x1b\xe8\xef%\x9e\xb6\xc4\x03\x07mZ\xe0>\xf4\xc1E7DmI\xae\xb3\xd7\xf5g\xeb\xf1!\x1f\x0f\xc8k-\x86\xee\xa2:m\t\xfc\xc8\xf5+\x97\xacK]K\xaay:{\xfa\x12\xad\xac>Z\xff\x88nN\x11\xf7\xe8\x86c\x90j\xd4\xed\xd6k<\xda\x15\x1d\x07u:yy\xe8\x0f\xa0?\xb0\x9e\xe9\xf0\x95\xca\xc8Xd\xfd\x0eC\x83\x88n\x18\xfd\xabRiiu\x1f#p\x05\xf7l}j\xac!D]\r\xe1B\xc5\x1e\xb8\xcaX\xf0\x98\xberM\xb5,|\xc3\x84\x13\xc5\xc7M\x0b\xa2\x0f\x94\x94\xf4O\xe6\x94\x04\x0fO\x08pz\x00c\xfc\xb45^o]\xf5\xff\x92[\xe6\x8e_\xcb\xfa\xb3\x8f\xd0\xfbk\x95\xf5P\x87\x0f\xab\xfc\x8a\x9c\xfa\x1c\xbc\xd8|\xa4\xf5\x9d$\xd4\xaa;\xba\xc6\xda}P\x1e}mc\xe8\xb9\xd3\x9f\x0fa\xab\xd8\x8b\xa5\x84\'\'\x1c\xf48\xba\xfe\xaf5\xe4\xd1\xb7\xb6\xc6\xf7\n'
>>> f = open(path+fn, "rb", encoding='utf-8')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    f = open(path+fn, "rb", encoding='utf-8')
ValueError: binary mode doesn't take an encoding argument
>>> f= io.BytesIO(path+fn, "rb", encoding='utf-8')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f= io.BytesIO(path+fn, "rb", encoding='utf-8')
TypeError: BytesIO() takes at most 1 argument (3 given)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> File "<pyshell#15>", line 1, in <module>
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> f=  io.FileIO(path+fn, mode='r', closefd=True)
>>> f
<_io.FileIO name='C:/Users/aalshobaki/Desktop/firewall/syslogs.gz' mode='rb' closefd=True>
>>> f.readline()
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x04\x00\xa4}Y\x92$;\x92\xdc?Ex\x87\xbc\xc0\x84`3,s\t\x9e\x81\xc2\xf9\xe6\x0f\xe7\xfeBS5\x8f\x0c\x98Gf\x06\x80\x92\x9e~=\xddU\xe5\xe5\t\x07\x0c\xb6\xe8\x92B\xec_\xff\xeb\xff\xfc\xf7W\xa8_\xa1\xfcg,\xff\x19\xf2\xd7\xff\xfb\xbf\xff\xfb\xbf\xbf\xeaW\x0c\x8f\x14\xfa#\x86\xf0\x88\xa5|\xfd\xc7\x97<\x8a<b\xd6\xffI\xf2W\xee)\xb4/\xa9Q\xba\xfeR\xec\xf2\xa8\xfa\xfbc}\xc4\xf1UJ\xfe\x9f\xff#\xfd\xfa\xe8\xd8\xbe\x9f\x9d\xda#\xa5\xe9\xd9\xed\xd1\xcbW\x96R\xc6W\x1a\xbdD<\xba%}n{\xe8\xff\xd5\xfa\xe9\xd1\xaf\xb7\x1e\xe9\xa1o\xf9|pI\x8fX\xd3\x97\x04\xd1\xdf)1e\xd1_J1?b\xaf\x8f\x9c\xf1\xd2=,\xbesN\x8f\x1c_O\xd6\xd5\x19\xed\xab\xa4!\xf2\x15S(xr\x19\x0f\x89\xfa;u5D_\xa9\x85\xf0\xe7\xc3\xbf\xdf:a\xad\xdbx=\\\x1f\x92\xf4\x87\x96\xac?z\xcc9\xf4\xe7k\xb7\xa2\x8f\x97GZ\\\x10\xfd:\x8f\xf1zn.\xba\xa4_"\xb9$}l\x0cI\x7fE\xbf`\x92\xc7\x10~\x90\xd5\xc5\xc0\xbb\xa4<\xdcj\xe0\'\x96\x12\xca\xd7\xa8\xa9\xe9\xaf\xe8G\x8d\xa2k\xf6\xa8\xba_\x966Fz\x8c\xf2\x98\xb6\x9c.C\x0f\xfaK\xba\x14Q\xb7\x05\xdeV?\xe1#\x95\xf2\x18\x8f\xf15R\\\xfdv\xfa\xe3\xc5\x96\xe7\xfd\xa6\xebPR\x89E\xf7[\x1e|\xb2\xee\x1c|8}xJ\xf8{\x96\xbe\x9c\xfe!}\xf8\xfc`\xfdo\xb9W\xd1\x8d\x1cG\xb1\xefV\x1f\x82%\xd3\xdf\xaa\x1b\xe8\xef%\x9e\xb6\xc4\x03\x07mZ\xe0>\xf4\xc1E7DmI\xae\xb3\xd7\xf5g\xeb\xf1!\x1f\x0f\xc8k-\x86\xee\xa2:m\t\xfc\xc8\xf5+\x97\xacK]K\xaay:{\xfa\x12\xad\xac>Z\xff\x88nN\x11\xf7\xe8\x86c\x90j\xd4\xed\xd6k<\xda\x15\x1d\x07u:yy\xe8\x0f\xa0?\xb0\x9e\xe9\xf0\x95\xca\xc8Xd\xfd\x0eC\x83\x88n\x18\xfd\xabRiiu\x1f#p\x05\xf7l}j\xac!D]\r\xe1B\xc5\x1e\xb8\xcaX\xf0\x98\xberM\xb5,|\xc3\x84\x13\xc5\xc7M\x0b\xa2\x0f\x94\x94\xf4O\xe6\x94\x04\x0fO\x08pz\x00c\xfc\xb45^o]\xf5\xff\x92[\xe6\x8e_\xcb\xfa\xb3\x8f\xd0\xfbk\x95\xf5P\x87\x0f\xab\xfc\x8a\x9c\xfa\x1c\xbc\xd8|\xa4\xf5\x9d$\xd4\xaa;\xba\xc6\xda}P\x1e}mc\xe8\xb9\xd3\x9f\x0fa\xab\xd8\x8b\xa5\x84\'\'\x1c\xf48\xba\xfe\xaf5\xe4\xd1\xb7\xb6\xc6\xf7\n'
>>> DD= io.TextIOBase(f, encoding = 'UTF-8')
>>> DD
<io.TextIOBase object at 0x03B95930>
>>> DD.readline()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    DD.readline()
io.UnsupportedOperation: readline
>>> DD.readline()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    DD.readline()
io.UnsupportedOperation: readline
>>> gzip.open(path+fn, 'rb').readline()
b'2018 Oct 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> gzip.open(path+fn, 'r').readline()
b'2018 Oct 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> gzip.open(path+fn, 'r').readline().decode('utf-8')
'2018 Oct 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> s=gzip.open(path+fn, 'r').readline().decode('utf-8')
>>> s
'2018 Oct 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> s2 =s
>>> c = re.sub(r'[a-zA-Z]', '', c)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c = re.sub(r'[a-zA-Z]', '', c)
NameError: name 'c' is not defined
>>> s =c = re.sub(r'(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1\2\3', s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s =c = re.sub(r'(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1\2\3', s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 944, in parse
    raise source.error("unbalanced parenthesis")
re.error: unbalanced parenthesis at position 37
>>> re.sub(r'(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1\2\3', s)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    re.sub(r'(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1\2\3', s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 944, in parse
    raise source.error("unbalanced parenthesis")
re.error: unbalanced parenthesis at position 37
>>> raise source.error("unbalanced parenthesis")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    raise source.error("unbalanced parenthesis")
NameError: name 'source' is not defined
>>> 
>>> 
>>> 
>>> 
>>> re.sub(r'(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1',s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    re.sub(r'(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1',s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 944, in parse
    raise source.error("unbalanced parenthesis")
re.error: unbalanced parenthesis at position 37
>>> thon\Python37-32\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
    
SyntaxError: unexpected character after line continuation character
>>> SyntaxError: unexpected character after line continuation character
SyntaxError: invalid syntax
>>> >>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):\d{2}):\d{2})', r'\1',s)
SyntaxError: invalid syntax
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', r'\1',s)
'2018 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', r'\1\2\3\4\5\6',s)
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> datetime
<class 'datetime.datetime'>
>>> datetime.strptime('2018 Nov 11 12:12:33', '%Y %b %d %HH:%MM%SS')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    datetime.strptime('2018 Nov 11 12:12:33', '%Y %b %d %HH:%MM%SS')
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 577, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 359, in _strptime
    (data_string, format))
ValueError: time data '2018 Nov 11 12:12:33' does not match format '%Y %b %d %HH:%MM%SS'
>>> datetime.strptime('2018 Nov 11 12:12:33', '%Y %b %d %H:%M%S')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    datetime.strptime('2018 Nov 11 12:12:33', '%Y %b %d %H:%M%S')
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 577, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 362, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: :33
>>> datetime.strptime('2018 Feb 11 12:12:33', '%Y %b %d %H:%M%S')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    datetime.strptime('2018 Feb 11 12:12:33', '%Y %b %d %H:%M%S')
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 577, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 362, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: :33
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', r'\1',s)re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', r'\1\2\3\4\5\6',s)
SyntaxError: invalid syntax
>>> 
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', datetime.strptime(r'\1\2\3\4\5\6','%Y%b%d%H:%M%S').strptime('%Y%m%d'),s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', datetime.strptime(r'\1\2\3\4\5\6','%Y%b%d%H:%M%S').strptime('%Y%m%d'),s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 577, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\_strptime.py", line 359, in _strptime
    (data_string, format))
ValueError: time data '\\1\\2\\3\\4\\5\\6' does not match format '%Y%b%d%H:%M%S'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', (r'\1\2\3\4\5\6').upper(),s)
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> upper('s')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    upper('s')
NameError: name 'upper' is not defined
>>> 
>>> 
>>> 's'.uper()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    's'.uper()
AttributeError: 'str' object has no attribute 'uper'
>>> s.upper()
'2018 OCT 06 04:14:03 SNAT 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', (r'\1\2\3\4\5\6').upper(),s)
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', ((r'\1\2\3\4\5\6').upper()),s)
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> '2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', max(r'\1\2\3\4\5\6'),s)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', max(r'\1\2\3\4\5\6'),s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 309, in _subx
    template = _compile_repl(template, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 300, in _compile_repl
    return sre_parse.parse_template(repl, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 954, in parse_template
    s = Tokenizer(source)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 232, in __init__
    self.__next()
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 246, in __next
    self.string, len(self.string) - 1) from None
re.error: bad escape (end of pattern) at position 0
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', len(r'\1\2\3\4\5\6'),s)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', len(r'\1\2\3\4\5\6'),s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 309, in _subx
    template = _compile_repl(template, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 300, in _compile_repl
    return sre_parse.parse_template(repl, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 954, in parse_template
    s = Tokenizer(source)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 228, in __init__
    string = str(string, 'latin1')
TypeError: decoding to str: need a bytes-like object, int found
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', len(str(r'\1\2\3\4\5\6')),s)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', len(str(r'\1\2\3\4\5\6')),s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 309, in _subx
    template = _compile_repl(template, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 300, in _compile_repl
    return sre_parse.parse_template(repl, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 954, in parse_template
    s = Tokenizer(source)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 228, in __init__
    string = str(string, 'latin1')
TypeError: decoding to str: need a bytes-like object, int found
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', str(r'\1\2\3\4\5\6'),s)
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> 
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', str(r'\1\2\3\4\5\6').upper(),s)
'2018Oct06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', str(r'\1len(\2)\3\4\5\6'),s)
'2018len(Oct)06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', len(str(r'\1\2\3\4\5\6')),s)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', len(str(r'\1\2\3\4\5\6')),s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 309, in _subx
    template = _compile_repl(template, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 300, in _compile_repl
    return sre_parse.parse_template(repl, pattern)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 954, in parse_template
    s = Tokenizer(source)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\sre_parse.py", line 228, in __init__
    string = str(string, 'latin1')
TypeError: decoding to str: need a bytes-like object, int found
>>> number_mapping = {'1': 'one',
                  '2': 'two',
                  '3': 'three'}
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', r'\1len(\2)\3\4\5\6'.upper(),s)
'2018LEN(Oct)06041403 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(2).upper(),s)
'OCT snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+x.group(2).upper(),s)
'2018OCT snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y'
							)
'01/25/13'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: datetime.strptime(x.group(1)+x.group(2)+x.group(2)+x.group(2)+x.group(2)+x.group(2)),,s)number_mapping
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> s
'2018 Oct 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> import re

number_mapping = {' Oct ': '10',
                  '2': 'two',
                  '3': 'three'}


print re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
SyntaxError: multiple statements found while compiling a single statement
>>> re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "<pyshell#97>", line 1, in <lambda>
    re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
KeyError: '201'
>>> number_mapping = {' Oct ': '10',
                  '2': 'two',
                  '3': 'three'}
>>> re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "<pyshell#99>", line 1, in <lambda>
    re.sub(r'\w{3}', lambda x: number_mapping[x.group()], s)
KeyError: '201'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})',number_mapping = {' Oct ': '10',
                  '2': 'two',
                  '3': 'three'}

	   }
SyntaxError: invalid syntax
>>> number_mapping = {'Oct': '10',
                  '2': 'two',
                  '3': 'three'}
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: number_mapping[x.group(2)], s)
'10 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b\d{4} (\w{3})', lambda x: number_mapping[x.group(2)], s)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    re.sub(r'\b\d{4} (\w{3})', lambda x: number_mapping[x.group(2)], s)
  File "C:\Users\aalshobaki\AppData\Local\Programs\Python\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "<pyshell#105>", line 1, in <lambda>
    re.sub(r'\b\d{4} (\w{3})', lambda x: number_mapping[x.group(2)], s)
IndexError: no such group
>>> re.sub(r'\b\d{4} (\w{3})', lambda x: number_mapping[x.group(1)], s)
'10 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> s
'2018 Oct 06 04:14:03 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)], s)+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1)+number_mapping[x.group(2)], s)+x.group(3)
SyntaxError: invalid syntax
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)], s)+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1)+number_mapping[x.group(2)], s)
SyntaxError: invalid syntax
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)], s)+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1), s)
SyntaxError: invalid syntax
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1),s)
'2018 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)], s)+x.group(3),s)
SyntaxError: invalid syntax
>>> e.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)]+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1)+number_mapping[x.group(2)], s)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    e.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)]+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1)+number_mapping[x.group(2)], s)
NameError: name 'e' is not defined
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)]+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1)+number_mapping[x.group(2)], s)
'20181006041403 201810 snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n'
>>> re.sub(r'\b(\d{4}) (\w{3}) (\d{2}) (\d{2}):(\d{2}):(\d{2})', lambda x: x.group(1)+number_mapping[x.group(2)]+x.group(3)+x.group(4)+x.group(5)+x.group(6)+' '+x.group(1)+number_mapping[x.group(2)]+x.group(3)+" '", s)
"20181006041403 20181006 ' snat 6 10.208.100.144 - 5.45.138.153 38207 56158 - 185.60.216.19 443\r\n"
>>> 
