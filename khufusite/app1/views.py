#encoding: utf-8
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.utils.encoding import smart_unicode,force_unicode,smart_str
try:
    import cmemcache as memcache
except:
    import memcache
import cjson
import hashlib
import os

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

def globalrequest(request):
    word,type_class = "",""
    return dict(word=word,
                type_class=type_class,
                menus=menus)

def isbot(request):
    botlist = [
        'Baiduspider',
        'Googlebot',
        'Yahoo! Slurp',
    ]
    for bot in botlist:
        if request.META['HTTP_USER_AGENT'].find(bot)==0:
            return True
    return False

def recomsearch(kids):
    """类似专题之类,固定uid输出的函数"""
    mc = memcache.Client(['114.113.30.29:11211'])
    for key in kids:
        d = mc.get(key)
        if d:
            d = cjson.decode(d)
            d["kid"]=key
            yield d

def hello(request):
    data = []
    mc = memcache.Client(['114.113.30.29:11212'])
    for m in menus:
        key = hashlib.md5(m).hexdigest()
        d = mc.get(key)
        if d:
            data.append( cjson.decode(d)[:4] )
    
    #专题的实现
    show_views=[
        "1918725321",
        "5710587117",
        "167035163130",
        "16549921536",
    ]
    data_view = recomsearch(show_views)
    
    #菜单下面的推荐位的实现
    recoms=[
        "1918725321",
        "5710587117",
        "167035163130",
        "16549921536",
        "9389121638",
        "16549921536",
        "6065323270",
        "7181029938",
    ]
    data_recoms = recomsearch(recoms)

    return render_to_response('index.html',locals(),
            context_instance=RequestContext(request))

def link(request):
    notbot = True
    if isbot(request):notbot = None
    return render_to_response('link.html',locals(),
        context_instance=RequestContext(request))

def keyword(request):
    word=request.GET["insearch"]
    page = 1
    if "page" in request.GET:
        page = request.GET["page"]
    type_class = "0"
    if "type_class" in request.GET:
        type_class=request.GET["type_class"]
    result=list(search(word,type_class))
    p = Paginator(result,20)
    pp = p.page(page)
    result1=pp.object_list[:10]
    result2=pp.object_list[10:]
    return render_to_response('search.html',locals())

def v(request,kid):
    mc = memcache.Client(['114.113.30.29:11211'])
    obj=cjson.decode(mc.get(str(kid)))
    #如果是机器人输出带拼音的正文
    if isbot(request):
        obj['memo']=obj['addpinyin']
    else:
        obj['memo']=obj['body']

    #相关新闻的实现
    from ngram import ngram
    rel_page = []
    tg = ngram(menus,min_sim=0.0)
    words = "||".join( tg.getSimilarStrings(smart_str(obj["title"],"utf8")).keys() )
    #相关新闻查询结果
    for kid2,obj2 in search(words,"0",num=10):
        rel_page.append( obj2['title'],kid2 )
    return render_to_response('info.html',locals(),
        context_instance=RequestContext(request))

def search(word,type_class,num=100):
    mc = memcache.Client(['114.113.30.29:11211'])
    word = smart_str(word,"utf8")
    type_class = smart_str(type_class,"utf8")
    if type_class!="0":
        word = " ".join( (word,type_class) )
    results=os.popen('dystmgr search -nl -max %s /home/yanxu/khufu/khufu %s' % (num,word) ).read()
    for kid in results.split('\n'):
        obj=mc.get(kid)
        if obj==None:continue
        yield kid,cjson.decode(obj)
