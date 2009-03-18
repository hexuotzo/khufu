#encoding: utf-8

from django import template
from django.template.defaultfilters import stringfilter

@stringfilter
def removetext(text):
    text=text.replace("-育儿早教-中国早教网","")
    text=text.replace("-怀孕胎教-中国早教网","")
    return text
