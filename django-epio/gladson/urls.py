# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "portal.views.index"),
    # Examples:
    # url(r'^$', 'gladson.views.home', name='home'),
    # url(r'^gladson/', include('gladson.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#if settings.SERVE_STATIC_FILES:
    #urlpatterns += patterns('',
        #(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            #{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    #)