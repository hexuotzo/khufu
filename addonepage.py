try:
    import cmemcache as memcache
except:
    import memcache
from addpinyin import *
import hashlib
import datetime
import cjson

url = ''
title = ''
text = '''

'''
pinyin = addpinyin(text)
now = datetime.datetime.now()

key = "%s" % hashlib.md5(url).hexdigest()
kid = string.atoi(key[:10],16)

mc = memcache.Client(['114.113.30.29:11211'])
dbvalue=cjson.encode({"title":ttl,"url":url,"html":text,"text":text,"datetime":str(nowtime),"addpinyin":pinyin,"body":text,"kid":kid})
mc.set(str(kid),dbvalue)

cmd = 'tctmgr put infodb/infodb %s "title" "%s" "savedate" "%s" "tag1" "%s"' % (kid,title,now.date(),'专家咨询')

