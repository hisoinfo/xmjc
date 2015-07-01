# -*- encoding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()



urlpatterns = [
    # Examples:
    url(r'^home/$', 'property.views.home', name='home'),
    url(r'^index/$', 'property.views.index', name='index'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
