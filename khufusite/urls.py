from django.conf.urls.defaults import *
from django.conf import settings

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
    (r'^hello','khufusite.app1.views.hello'),
    (r'^top','khufusite.app1.views.top'),
    (r'^bottom','khufusite.app1.views.bottom'),
    (r'^keyword','khufusite.app1.views.keyword'),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/Users/uc0079/khufu/khufusite/html/media/images'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/Users/uc0079/khufu/khufusite/html/media/css'}),
    #(r'$','khufusite.app1.views.index'),
    (r'comments/',include('django.contrib.comments.urls'))
)
