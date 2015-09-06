from django.conf.urls import patterns, include, url
from django.contrib import admin
from TouchSave_App import views

admin.autodiscover()

urlpatterns = [
    url(r'^TouchSave/', include('TouchSave_App.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('TouchSave_App.urls')),
    url(r'^TouchSave/profile/$',views.profile, name='profle'),
]
