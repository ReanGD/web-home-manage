from django.conf.urls import patterns, url

from manage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^films/$', views.films, name='films'),
    url(r'^audiobook/$', views.audiobook, name='audiobook'),
)
