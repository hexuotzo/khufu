# encoding: utf-8
import os,sys
import hashlib
import cjson
import datetime
import re
from html2text import html2text

def findpath(path):
    #dir:文件夹名 
    #subdir子文件夹 
    #files所有文件
    for d,subdir,files in os.walk(path): 
        for f in files:
            yield d,f

def readtext(f):
    try:
        r=open(fname).read().decode('utf8')
    except:
        try:
            r=open(fname).read().decode('gbk')
        except:
            r=u''
    return r

def readtitle(fname):
    s=open(fname).read()
    s=s.strip()
    for title in re.findall(r'<title>(.*)</title>',s):
        return title    

path = sys.argv[1]
for d,f in findpath(path):
    fname = os.path.join(d,f)
    r=readtext(fname)
    if r=='':continue
    try:
        text = html2text(r).replace('"','')
    except:
        text = r.replace('"','')
    key = "1%s" % hashlib.md5(fname).hexdigest()
    nowtime=datetime.datetime.now()
    ttl = readtitle(fname)
    dbvalue=cjson.encode({"title":ttl,"url":fname,"html":r,"text":text,"datetime":str(nowtime)})
    dbvalue = dbvalue.replace('"','')
    os.popen('dystmgr put khufu %s "%s"'%(key,text.encode('utf8'))).read()
    os.popen('tchmgr put metaDB.tch %s "%s"'%(key,dbvalue)).read()
    print key
    