#encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
try:
    import cmemcache as memcache
except:
    import memcache
import cjson
import hashlib
import os


def hello(request):
    menus = [
        "备孕",
        "怀孕",
        "产后",
        "0-1岁",
        "1-2岁",
        "2-3岁",
        "3-6岁",
        "专家咨询",
    ]
    show_views=[
        "1918725321",
        "5710587117",
        "167035163130",
        "16549921536",
    ]
    data = []
    data_view = []
    mc = memcache.Client(['114.113.30.29:11212'])
    mc2 = memcache.Client(['114.113.30.29:11211'])
    for m in menus:
        key = hashlib.md5(m).hexdigest()
        d = mc.get(key)
        if d:
            data.append( cjson.decode(d)[:4] )
    for key in show_views:
        d = mc2.get(key)
        if d:
            d = cjson.decode(d)
            d["kid"]=key
            data_view.append( d )
    return render_to_response('index.html',locals())
    
def link(request):
    return render_to_response('link.html',locals())

def keyword(request):
    word=request.GET["insearch"]
    result=list(tmpsearch(word))
    result1=result[:10]
    result2=result[10:]
    return render_to_response('search.html',locals())

def v(request,kid):
    mc = memcache.Client(['114.113.30.29:11211'])
    obj=cjson.decode(mc.get(str(kid)))
    
    from ngram import ngram
    menus = [
        "备孕",
        "怀孕",
        "产后",
        "0-1岁",
        "1-2岁",
        "2-3岁",
        "3-6岁",
        "专家咨询",
    ]
    rel_page = []
    tg = ngram(menus,min_sim=0.0)
    words = "||".join( (tg.getSimilarStrings(obj["title"].encode("utf8"))).keys() )
    results=os.popen('dystmgr search -nl -max 10 /home/yanxu/khufu/khufu %s'%words).read()
    for kid2 in results.split('\n'):
        obj2=mc.get(kid2)
        if obj2==None:continue
        tmp=cjson.decode(obj2)
        rel_page.append( (tmp['title'],kid2) )
    return render_to_response('info.html',locals())
    
def tmpsearch(word):
    word=word.encode("utf8")
    mc = memcache.Client(['114.113.30.29:11211'])
    results=os.popen('dystmgr search -nl -max 20 /home/yanxu/khufu/khufu "%s"'%word).read()
    for kid in results.split('\n'):
        obj=mc.get(kid)
        if obj==None:continue
        tmp=cjson.decode(obj)
        yield tmp['title'],tmp['addpinyin'],kid
