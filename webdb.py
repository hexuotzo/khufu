#!/usr/local/bin/python
# encoding: utf-8
try:
    import cmemcache as memcache
except ImportError:
    import memcache
import cjson
import sys,os,hashlib
import pycabinet as pb
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
    data = pb.search('114.113.30.29',11214,'tag1',word,500,0,0)
    if len(data)==0:
        data = pb.search('114.113.30.29',11214,'tag1','怀孕',500,0,0)
    for i in range(10):
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
