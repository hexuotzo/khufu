#!/usr/local/bin/python
# encoding: utf-8
from pykhufu import PyDystopia
import cmemcache as memcache
import cjson
import sys,os,hashlib

MENU = [
    "备孕",
    "怀孕",
    "分娩期",
    "0-1岁",
    "1-2岁",
    "2-3岁",
    "3-6岁",
    "专家咨询",
]

def removetext(text):
    text = text.encode('utf8')
    return text.replace('-育儿早教-中国早教网','')

def search(word):
    for kid in os.popen('dystmgr search -nl khufu %s' % word).read().split('\n'):
        if kid=='':continue
        obj = cjson.decode(mc.get(kid))
        d = dict(
            title = unicode(removetext(obj['title']),'utf8'),
            kid = kid
        )
        yield kid,d

def words():
    if len(sys.argv)>1:
        word = sys.argv[1].strip()
        yield word
    else:
        for word in MENU:
            yield word

mc = memcache.Client(['114.113.30.29:11211'])
mc2 = memcache.Client(['114.113.30.29:11212'])
for word in words():
    print word
    data = [d for kid,d in search(word)]
    obj = cjson.encode(data)
    k = hashlib.md5(word).hexdigest()
    mc2.set(k,obj)
