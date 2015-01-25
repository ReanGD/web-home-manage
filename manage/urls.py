from django.conf.urls import patterns, url

from manage import views, forms

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get/films/$', views.get_films),
    url(r'^get/audiobooks/$', views.get_audiobooks),

    url(r'^get/local_storage/$', views.local_storage,
        name='get_local_storage'),
    url(r'^form/local_storage/$', forms.local_storage,
        name='form_local_storage'),
    url(r'^form/local_storage/(?P<id>\d+)$', forms.local_storage,
        name='form_local_storage'),

    url(r'^get/remote_storage/$', views.remote_storage,
        name='get_remote_storage'),
    url(r'^form/remote_storage/$', forms.remote_storage,
        name='form_remote_storage'),
    url(r'^form/remote_storage/(?P<id>\d+)$', forms.remote_storage,
        name='form_remote_storage'),

    url(r'^get/storage_map/$', views.storage_map,
        name='get_storage_map'),
    url(r'^form/storage_map/$', forms.storage_map,
        name='form_storage_map'),
    url(r'^form/storage_map/(?P<id>\d+)$', forms.storage_map,
        name='form_storage_map'),
)
