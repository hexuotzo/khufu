#!/usr/local/bin/python
# encoding: utf-8
try:
    import cmemcache as memcache
except ImportError:
    import memcache
import cjson
import sys,os,hashlib

MENU = [
    "备孕",
    "怀孕",
    "产后",
    "0-1岁",
    "1-2岁",
    "2-3岁",
    "3-6岁",
    # "专家咨询",
]

def search(word):
    if word=='3-6岁':
        for kid in ['508111489111',
                    '509210323473',
                    '513616214258',
                    '516076124350']:
            d=mc.get(kid)
            if d:
                d=cjson.decode(d)
                yield kid,{"kid":kid,"title":d["title"]}
    elif word=='1-2岁':
        for kid in ['25958321621',
                    '28294915184',
                    '29934388407',
                    '32830901239']:
            d=mc.get(kid)
            if d:
                d=cjson.decode(d)
                yield kid,{"kid":kid,"title":d["title"]}
    else:
        for text in os.popen('tctmgr search -pv -ord savedate numdesc -m 4 infodb/infodb tag1 STRBW "%s"' % word ).read().split('\n'):
            text = text.split("\t")
            if len(text)<>7:continue
            kid,p1,title,p2,savedate,p3,tag1 = text
            print kid,title
            yield kid,{"kid":kid,"title":unicode(title,"utf8")}

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
