from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from torrents import views

router = DefaultRouter()
router.register(r'remote_torrents', views.RemoteTorrentList)
router.register(r'local_torrents', views.LocalTorrentList)

schema_view = get_swagger_view(title='Torrents API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
