from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import KhufuForm
from pykhufu import PyDystopia
from subprocess import Popen,PIPE
try:
    import cmemcache as memcache
except:
    import memcache
import cjson
import os


def hello(request):
    try:
        f = KhufuForm.objects.get(id=1)
    except:
        f = KhufuForm.objects.create(id=1)
    return render_to_response('index.html',locals())
    
def top(request):
    return render_to_response('top.html',locals())
    
def bottom(request):
    return render_to_response('bottom.html',locals())

def keyword(request):
    word=request.GET["insearch"]
    result=tmpsearch(word)
    return render_to_response('result.html',locals())

def v(request,kid):
    mc = memcache.Client(['61.135.214.29:11211'])
    obj=cjson.decode(mc.get(kid))['addpinyin']
    return HttpResponse("<pre>%s</pre>"%obj)
    
def tmpsearch(word):
    word=word.encode("utf8")
    mc = memcache.Client(['61.135.214.29:11211'])
    results=os.popen('dystmgr search -nl -max 10 khufu "%s"'%word).read()
    for kid in results.split('\n'):
        obj=mc.get(kid)
        print "kid",kid
        if obj==None:continue
        tmp=cjson.decode(obj)
        yield tmp['title'],tmp['addpinyin'],kid
