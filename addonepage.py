# encoding: utf-8
try:
    import cmemcache as memcache
except:
    import memcache
from addpinyin import *
import hashlib
import datetime
import cjson
import string

url = ''
tag = '专家咨询'
title = ''
text = '''

'''
pinyin = addpinyin(text)
now = datetime.datetime.now()

key = "%s" % hashlib.md5(url).hexdigest()
kid = string.atoi(key[:10],16)

print kid,title

mc = memcache.Client(['114.113.30.29:11211'])
dbvalue=cjson.encode({"title":title,"url":url,"html":text,"text":text,"datetime":str(nowtime),"addpinyin":pinyin,"body":text,"kid":kid})
mc.set(str(kid),dbvalue)

cmd = 'tctmgr put infodb/infodb %s "title" "%s" "savedate" "%s" "tag1" "%s"' % (kid,title,now.date(),tag)

