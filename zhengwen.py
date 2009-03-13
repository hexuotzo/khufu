# encoding: utf-8
import os
from html2text import html2text
url = "http://baby.sina.com.cn/nutrition/09/1203/0817133159.shtml"
html = os.popen("curl --compressed %s" % url).read()
body=[]
try:
    txt = html2text(html.decode('utf8'))
except:
    txt = html2text(html.decode('gbk'))
try:
    txt = txt.encode('utf8').split('\n')
except:
    txt = txt.encode('gbk').split('\n')
for r in txt:
    r = r.strip()
    if r == '':continue
    elif r[0]=='[':pass
    elif r[0].isdigit() and r[2]>chr(127):print r
    elif r[0]=='#':print r
    elif r[0]== '*' and r[1]=='*': print r
    elif r[0]>chr(127):print r