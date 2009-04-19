# encoding: utf-8
import os,sys
import hashlib
import datetime
import re
import string
import glob
from bodytext import getbody


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
for fname in findpath(path):
    c1 = docclass.naivebayes(docclass.getwords)
    if fname.find("article")==-1:continue
    r=readtext(fname)
    if r=='':continue
    key = "%s" % hashlib.md5(fname).hexdigest()
    kid=string.atoi(key[:10],16)
    nowtime=datetime.datetime.now()
    print "key",key,kid,fname
    try:
        body = getbody(r.encode("utf8"))
    except:
        continue
    title = readtitle(fname)
    cmd = 'tctmgr put infodb/infodb %s "title" "%s" "savedate" "%s" "tag1" "%s"' % (kid,title,nowtime.date(),c1.classify(body))
    print os.popen(cmd).read()
    