from django.conf.urls import patterns, include, url
from day1 import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn.views.home', name='home'),
    # url(r'^learn/', include('learn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^text/', views.some_text),
    url(r'^multiply/(?P<num1>\d+)/(?P<num2>\d+)/$', views.multiply_numbers),
)
