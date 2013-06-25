from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^day1/', include('day1.urls')),
)
