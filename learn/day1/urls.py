from django.conf.urls import patterns, include, url
from day1 import views

urlpatterns = patterns('',
    url(r'^text/', views.some_text),
    url(r'^multiply/(?P<num1>\d+)/(?P<num2>\d+)/$', views.multiply_numbers),
    # INSERT YOUR NEW URL PATTERN FOR TASK 2 BELOW
    

    # INSERT YOUR NEW URL PATTERN FOR TASK 2 ABOVE
)
