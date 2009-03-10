#!/usr/local/bin/python
# encoding: utf-8
from pykhufu import PyDystopia
import cmemcache as memcache
import cjson
import sys,os

def removetext(text):
    text = text.encode('utf8')
    return text.replace('-育儿早教-中国早教网','')

word = sys.argv[1]
mc = memcache.Client(['61.135.214.29:11211'])
mc2 = memcache.Client(['61.135.214.29:11212'])
for kid in os.popen('dystmgr search -nl khufu %s' % word).read().split('\n'):
    if kid=='':continue
    print kid
    obj = cjson.decode(mc.get(kid))
    obj2 = cjson.encode(dict(
        title = removetext(obj['title']),
        kid = kid
    ))
    mc2.set(kid,obj2)
    