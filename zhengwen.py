# encoding: utf-8
import os
from html2text import html2text
bodyss=[]
url = "http://www.zaojiao.com/education/2008/1120/article_2079.html"
html = os.popen("curl --compressed %s" % url).read()
try:
    txt = html2text(html.decode('utf8'))
except:
    txt = html2text(html.decode('gbk'))
try:
    txt = txt.encode('utf8').split('\n')
except:
    txt = txt.encode('gbk').split('\n')
for r in txt:
    try:
        r = r.strip().decode('utf8')
    except:
        r = r.strip().decode('gbk')
    if r == '':continue
    elif type(r[0])==int:bodyss.append(r)
    #elif type(r[0])==str:yield r
    elif r[0]== '*' and r[1]=='*': bodyss.append(r)
print bodyss
