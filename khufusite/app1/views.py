# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import KhufuForm
from pykhufu import PyDystopia
import os


def hello(request):
    print 'a'
    try:
        f = KhufuForm.objects.get(id=1)
    except:
        f = KhufuForm.objects.create(id=1)
    return render_to_response('index.html',locals())
    
def keyword(request):
    print "b"
    word=request.GET["insearch"]
    print "c"
    result=tmpsearch(word)
    print "d"
    return render_to_response('result.html',locals())
    
def tmpsearch(word):
    word=word.encode("utf8")
    pd = PyDystopia('/Users/uc0079/khufu/tmpa/dystopia')
    print "e"
    for kid in pd.search(word):
        print "f"
        print "kid",kid
        tmp=cjson.decode(os.popen("tchmgr get /Users/uc0079/khufu/tmpa/metaDB.tch %s"%kid).read())
        print tmp['title']
        yield tmp['title'],tmp['url'],tmp['text'][:100]
    