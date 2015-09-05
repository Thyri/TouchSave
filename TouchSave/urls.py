from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^TouchSave/', include('ToolShare.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('ToolShare.urls'))
)
