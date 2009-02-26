# encoding: utf-8
import os,sys
import hashlib
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

path = sys.argv[1]
for d,f in findpath(path):
    fname = os.path.join(d,f)
    r=readtext(fname)
    if r=='':continue
    text = html2text(r).replace('"','')
    key = hashlib.md5(fname).hexdigest()
    print os.popen('dystmgr put khufu 1%s "%s"'%(key,text.encode('utf8'))).read()
               