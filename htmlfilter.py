# encoding: utf-8
import os,sys
import hashlib
import cjson
import datetime
import re
from pykhufu import PyDystopia
import cmemcache as memcache
from html2text import html2text
from addpinyin import *
from bodytext import getbody
import string
import glob

def findpath(path):
    #dir:文件夹名 
    #subdir子文件夹 
    #files所有文件
    for d,subdir,files in os.walk(path):
        for f in glob.glob(os.path.join(d,"*.html")):
        #for f in files:
            yield f

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
        try:
            return title.decode('utf8')
        except:
            return title
    return u''

path = sys.argv[1]
pd = PyDystopia()
mc = memcache.Client(['114.113.30.29:11211'])
for fname in findpath(path):
    #fname = os.path.join(d,f)
    if fname.find("article")==-1:continue
    r=readtext(fname)
    if r=='':continue
    key = "%s" % hashlib.md5(fname).hexdigest()
    kid=string.atoi(key[:10],16)
    nowtime=datetime.datetime.now()
    print "key",key,kid,fname
    try:
        text = html2text(r)
        body = getbody(r.encode("utf8"))
    except:
        continue
    ttl = readtitle(fname)
    pinyin = addpinyin(body)
    dbvalue=cjson.encode({"title":ttl,"url":fname,"html":r,"text":text,"datetime":str(nowtime),"addpinyin":pinyin,"body":body})
    pd.put(kid,text.encode('utf8'))
    mc.set(str(kid),dbvalue)
pd.commit()
