from django.conf.urls import patterns, url

from manage import views, forms

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get/films/$', views.get_films),
    url(r'^get/audiobooks/$', views.get_audiobooks),

    url(r'^local_storage/list/$', forms.local_storage,
        {'action': 'list'}, 'local_storage_list'),
    url(r'^local_storage/add/$', forms.local_storage,
        {'action': 'add'}, 'local_storage_add'),
    url(r'^local_storage/edit/(?P<id>\d+)$', forms.local_storage,
        {'action': 'edit'}, name='local_storage_edit'),
    url(r'^local_storage/delete/(?P<id>\d+)$', forms.local_storage,
        {'action': 'delete'}, name='local_storage_delete'),

    url(r'^remote_storage/list/$', forms.remote_storage,
        {'action': 'list'}, 'remote_storage_list'),
    url(r'^remote_storage/add/$', forms.remote_storage,
        {'action': 'add'}, 'remote_storage_add'),
    url(r'^remote_storage/edit/(?P<id>\d+)$', forms.remote_storage,
        {'action': 'edit'}, name='remote_storage_edit'),
    url(r'^remote_storage/delete/(?P<id>\d+)$', forms.remote_storage,
        {'action': 'delete'}, name='remote_storage_delete'),

    url(r'^storage_map/list/$', forms.storage_map,
        {'action': 'list'}, 'storage_map_list'),
    url(r'^storage_map/add/$', forms.storage_map,
        {'action': 'add'}, 'storage_map_add'),
    url(r'^storage_map/edit/(?P<id>\d+)$', forms.storage_map,
        {'action': 'edit'}, name='storage_map_edit'),
    url(r'^storage_map/delete/(?P<id>\d+)$', forms.storage_map,
        {'action': 'delete'}, name='storage_map_delete'),
)
