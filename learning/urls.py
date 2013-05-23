from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'app1.views.not_found'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning.views.home', name='home'),
    url(r'^app1/', include('app1.urls', namespace='app1')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
