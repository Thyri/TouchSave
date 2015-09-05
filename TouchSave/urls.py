from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^TouchSave/', include('TouchSave_App.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('TouchSave_App.urls')),
]
