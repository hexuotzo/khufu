from django.conf.urls.defaults import *

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
    (r'^keyword','khufusite.app1.views.keyword'),
    #(r'$','khufusite.app1.views.index'),
    (r'comments/',include('django.contrib.comments.urls'))
)
