from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from khufusite.app1.sitemap import BlogSitemap
from khufusite.app1.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
}



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()



urlpatterns = patterns('',
    # Example:
    # (r'^khufusite/', include('khufusite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$','khufusite.app1.views.hello'),
    (r'^hello','khufusite.app1.views.hello'),
    (r'^keyword','khufusite.app1.views.keyword'),
    (r'^link','khufusite.app1.views.link'),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/yanxu/khufu/khufusite/media/images'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/yanxu/khufu/khufusite/media/css'}),
    (r'^v/(?P<kid>.*)/','khufusite.app1.views.v'),
    #(r'$','khufusite.app1.views.index'),
    (r'comments/',include('django.contrib.comments.urls')),
    
    (r'^rss/', 'khufusite.app1.rss.rss'),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    #(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),    
    )