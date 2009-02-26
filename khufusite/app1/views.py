# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os

def hello(request):
    return render_to_response('index.html',locals())
def keyword(request):
    word=request.GET["insearch"]
    print tmpsearch(word)
def tmpsearch(word):
    tmp=os.popen("dystmgr search -pv khufu %s"%word).read()
    return tmp.split('\n')