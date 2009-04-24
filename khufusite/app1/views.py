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
    domain = settings.DOMAIN
    return dict(word=word,
                type_class=type_class,
                menus=menus,
                domain=domain)

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

def recomsearch(mcip,func):
    """类似专题之类,固定uid输出的函数"""
    mc = memcache.Client([mcip])
    def wapper(kids,flag=False):
        data = []
        for key in kids:
            if flag:
                key = hashlib.md5(key).hexdigest()
            d = mc.get(key)
            if d:
                d = cjson.decode(d)
                d2 = func(d,key)
                if d2:
                    data.append(d2)
                else:
                    data.append(d)
        return data
    return wapper
mc11211 = recomsearch('114.113.30.29:11211',lambda x,key:x.__setitem__("kid",key))
mc11212 = recomsearch('114.113.30.29:11212',lambda x,key:x.__getslice__(0,4))

def hello(request):
    data = mc11212(menus,True)

    #专题的实现
    show_views=[
        "1918725321",
        "5710587117",
        "167035163130",
        "16549921536",
    ]
    data_view = mc11211(show_views)
    
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
    data_recoms = mc11211(recoms)

    return render_to_response('index.html',locals(),
            context_instance=RequestContext(request))

def link(request):
    notbot = True
    if isbot(request):notbot = None
    return render_to_response('link.html',locals(),
        context_instance=RequestContext(request))

def keyword(request):
    if "insearch" in request.GET:
        word=request.GET["insearch"]
    page = 1
    if "page" in request.GET:
        page = request.GET["page"]
    type_class = "0"
    if "type_class" in request.GET:
        type_class=request.GET["type_class"]
    result=list(search(word,type_class,2000))
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
    keys = tg.getSimilarStrings(smart_str(obj["title"],"utf8")).keys()
    title = " ".join( keys )
    words = "||".join( keys )
    #相关新闻查询结果
    for kid2,obj2 in search(words,"0",num=10):
        rel_page.append( (obj2['title'],kid2) )
    return render_to_response('info.html',locals(),
        context_instance=RequestContext(request))

def search(word,type_class,num=1000):
    word = smart_str(word,"utf8")
    type_class = smart_str(type_class,"utf8")
    if type_class!="0":
        word = " ".join( (word,type_class) )
    results=os.popen('tctmgr search -pv -ord savedate numdesc /home/yanxu/khufu/infodb/infodb tag1 STRBW "%s"' % word ).read()
    if results=='':
        # mc = memcache.Client(['114.113.30.29:11211'])
        results = os.popen('dystmgr search -nl -max %s /home/yanxu/khufu/khufu %s' % (num,word)).read()
    for text in results.split('\n'):
        if text.isdigit():
            kid = text
            text = os.popen('tctmgr get -pz /home/yanxu/khufu/infodb/infodb %s' % text).read().strip()
        text = text.split("\t")
        if len(text)==7:
            kid,p1,title,p2,savedate,p3,tag1 = text
        elif len(text)==6:
            p1,title,p2,savedate,p3,tag1 = text
        else:
            continue
        yield kid,{"title":title}


def google9b196a21d9a447d9(request):
    return HttpResponse(open('/home/yanxu/khufu/khufusite/media/html/google9b196a21d9a447d9.html').
    read())

