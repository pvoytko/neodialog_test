# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

# Скрываем админку для этих моделей
admin.autodiscover()
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'man.views.home'),
    # url(r'^nd/', include('nd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'', include(admin.site.urls)),
)

