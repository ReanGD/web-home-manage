from django.conf.urls import patterns, url

from manage import views, forms

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^get/films/$', views.get_films),
    url(r'^get/audiobooks/$', views.get_audiobooks),
    url(r'^get/local_storage/$', views.get_local_storage),
    url(r'^(?P<job_id>\d+)/settings_save/$', forms.local_storage_add),
    url(r'^get/remote_storage/$', views.get_remote_storage),
    url(r'^get/settings/$', views.get_settings),
)
