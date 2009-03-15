# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from pykhufu import PyDystopia
try:
    import cmemcache as memcache
except:
    import memcache
import cjson
import os


def hello(request):
    menus = [
        "备孕",
        "怀孕",
        "分娩期",
        "0-1岁",
        "1-2岁",
        "2-3岁",
        "3-6岁",
        "专家咨询",
    ]
    data = []
    mc = memcache.Client(['114.113.30.29:11212'])
    for m in menus:
        key = hashlib.md5(m).hexdigest()
        d = mc.get(key)
        if d:
            data.append( cjson.decode(d)[:4] )
    return render_to_response('index.html',locals())
    
def top(request):
    return render_to_response('top.html',locals())
    
def bottom(request):
    return render_to_response('bottom.html',locals())

def keyword(request):
    word=request.GET["insearch"]
    result=tmpsearch(word)
    return render_to_response('search.html',locals())

def v(request,kid):
    mc = memcache.Client(['114.113.30.29:11211'])
    obj=cjson.decode(mc.get(str(kid)))
    return render_to_response('info.html',locals())
    
def tmpsearch(word):
    word=word.encode("utf8")
    mc = memcache.Client(['114.113.30.29:11211'])
    results=os.popen('dystmgr search -nl -max 10 /Users/uc0079/khufu/khufu "%s"'%word).read()
    print "result:",results
    for kid in results.split('\n'):
        print kid
        obj=mc.get(kid)
        print "kid",kid
        if obj==None:continue
        tmp=cjson.decode(obj)
        yield tmp['title'],tmp['addpinyin'],kid
