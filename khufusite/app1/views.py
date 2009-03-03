# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import KhufuForm
import os

def hello(request):
    print 'a'
    try:
        f = KhufuForm.objects.get(id=1)
    except:
        f = KhufuForm.objects.create(id=1)
    return render_to_response('index.html',locals())
    
def keyword(request):
    word=request.GET["insearch"]
    result=tmpsearch(word)
    return render_to_response('result.html',locals())
    
def tmpsearch(word):
    word=word.encode("utf8")
    tmp=os.popen("dystmgr search -pv /Users/uc0079/khufu/khufu/ %s"%word).read()
    return tmp.split('\n')