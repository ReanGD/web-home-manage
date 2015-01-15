from django.conf.urls import patterns, url

from manage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get/films/$', views.get_films, name='get_films'),
    url(r'^get/audiobooks/$', views.get_audiobooks, name='get_audiobooks'),
)
