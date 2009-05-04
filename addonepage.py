# encoding: utf-8
try:
    import cmemcache as memcache
except:
    import memcache
from addpinyin import *
import datetime
import cjson
import os
import uid

url = ''
tag = '专家咨询'
title = u''
text = u'''

'''
pinyin = addpinyin(text)
now = datetime.datetime.now()

kid = uid.getKid(url)
print kid,title

mc = memcache.Client(['114.113.30.29:11211'])
dbvalue=cjson.encode({"title":title,"url":url,"html":text,"text":text,"datetime":str(now),"addpinyin":pinyin,"body":text,"kid":kid})
mc.set(str(kid),dbvalue)

cmd = 'tctmgr put infodb/infodb %s "title" "%s" "savedate" "%s" "tag1" "%s"' % (kid,title.encode("utf8"),now.date(),tag)
print os.popen(cmd).read()
