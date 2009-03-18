#encoding: utf-8

from django import template

register = template.Library()

@register.filter
def removetext(text):
    text=text.replace("-育儿早教-中国早教网","")
    text=text.replace("-怀孕胎教-中国早教网","")
    return text
