#encoding: utf-8
from django.http import HttpResponse,Http404
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
import pycabinet as pb

def globalrequest(request):
    word,type_class = "",""
    domain = "http://%s" % settings.DOMAIN
    media_url = settings.MEDIA_URL
    return dict(word=word,
                type_class=type_class,
                menus=settings.MENUS,
                domain=domain,
                media_url=media_url)

def isbot(request):
    for bot in settings.BOTLIST:
        if request.META['HTTP_USER_AGENT'].find(bot)==0:
            return True
    return False

def search(port,field,value,maxnum):
    value = smart_str(value,"utf8")
    return pb.search(settings.MC_IP,port,field,value,maxnum)

def searchdata(field,value,maxnum):
    data = search(settings.MC_DATA_PORT,field,value,maxnum)
    for d in data:
        yield d

def searchinfo(field,value,maxnum):
    data = search(settings.MC_INFO_PORT,field,value,maxnum)
    for d in data:
        yield d

def getDataByKid(kid):
    try:
        return list(searchinfo("kid",kid,1))[0]
    except:
        return ""

def getDataByKids(kids):
    for kid in kids:
        d = getDataByKid(kid)
        yield d

def getDataByMenus(menus):
    mc = memcache.Client(["%s:%s" % (settings.MC_IP,settings.MC_MENU_PORT)])
    for menu in menus:
        key = hashlib.md5(menu).hexdigest()
        d = mc.get(key)
        if d:
            d = cjson.decode(d)
            yield d

def hello(request):
    data = list(getDataByMenus(settings.MENUS))
    
    #专题的实现
    data_view = list(getDataByKids(settings.TOP_VIEWS))
    #菜单下面的推荐位的实现
    data_recoms = list(getDataByKids(settings.RECOMS))
    
    return render_to_response('index.html',locals(),
            context_instance=RequestContext(request))

def link(request):
    notbot = True
    if isbot(request):notbot = None
    return render_to_response('link.html',locals(),
        context_instance=RequestContext(request))

def keyword(request):
    page = 1
    type_class = "0"
    if "insearch" in request.GET:
        word=request.GET["insearch"]
    if "page" in request.GET:
        page = request.GET["page"]
    if "type_class" in request.GET:
        type_class=request.GET["type_class"]
    result=list(searchinfo("tag1",word,5000))
    p = Paginator(result,20)
    pp = p.page(page)
    result1=pp.object_list[:10]
    result2=pp.object_list[10:]
    return render_to_response('search.html',locals(),
        context_instance=RequestContext(request))

def v(request,kid):
    try:
        obj=getDataByKid('kid',kid,1)
    except:
        raise Http404
    #如果是机器人输出带拼音的正文
    if isbot(request):
        obj['memo']=obj['addpinyin']
    else:
        obj['memo']=obj['text']
        
    #相关新闻的实现
    from ngram import ngram
    rel_page = []
    tg = ngram(menus,min_sim=0.0)
    keys = tg.getSimilarStrings(smart_str(obj["title"],"utf8")).keys()
    title = " ".join( keys )
    words = "||".join( keys )
    #相关新闻查询结果
    # for kid2,obj2 in search(words,"0",num=10):
    #     rel_page.append( (obj2['title'],kid2) )
    return render_to_response('info.html',locals(),
        context_instance=RequestContext(request))

def google9b196a21d9a447d9(request):
    return HttpResponse(open('/home/yanxu/khufu/khufusite/media/html/google9b196a21d9a447d9.html').
    read())

