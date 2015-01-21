from django.conf.urls import patterns, url

from manage import views, forms

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get/films/$', views.get_films),
    url(r'^get/audiobooks/$', views.get_audiobooks),
    url(r'^get/local_storage/$', views.get_local_storage),
    url(r'^save/local_storage/$', forms.save_local_storage,
        name='save_local_storage'),
    url(r'^get/remote_storage/$', views.get_remote_storage),
    url(r'^save/remote_storage/$', forms.save_remote_storage,
        name='save_remote_storage'),
    url(r'^get/settings/$', views.get_settings),
)
