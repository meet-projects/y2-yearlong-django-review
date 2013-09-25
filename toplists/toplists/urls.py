from django.conf.urls import patterns, include, url

from movies import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^movies$', 'views.movie_list'),
    url(r'^movies/(?P<movie_id>\d+)', 'views.movie'),
    url(r'^movies/(?P<movie_id>\d+)/addcomment', 'views.add_comment'),
    url(r'^movies/(?P<movie_id>\d+)/like', 'views.like'),
    url(r'^movies/(?P<movie_id>\d+)/dislike', 'views.dislike')
)
