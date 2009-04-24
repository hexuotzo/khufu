#!/usr/local/bin/python
# encoding: utf-8
try:
    import cmemcache as memcache
except ImportError:
    import memcache
import cjson
import sys,os,hashlib
import pycabinet
import random

MENU = [
    "备孕",
    "怀孕",
    "产后",
    "0-1岁",
    "1-2岁",
    "2-3岁",
    "3-6岁",
    "专家咨询",
]

def search(word):
    data = pycabinet.search('/home/yanxu/khufu/infodb/infodb','tag1','怀孕',1000)
    for i in range(4):
        obj = random.choice(data)
        kid,title = obj["kid"],unicode(obj["title"],"utf8")
        print kid,title
        yield kid,{'title':title,'kid':kid}

def words():
    if len(sys.argv)>1:
        word = sys.argv[1].strip()
        yield word
    else:
        for word in MENU:
            yield word

# mc = memcache.Client(['114.113.30.29:11211'])
mc2 = memcache.Client(['114.113.30.29:11212'])
for word in words():
    print word
    data = [d for kid,d in search(word)]
    if data>0:
        obj = cjson.encode(data)
        k = hashlib.md5(word).hexdigest()
        mc2.set(k,obj)
