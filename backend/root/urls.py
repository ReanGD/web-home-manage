from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from torrents import urls


schema_view = get_swagger_view(title='Torrents API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^api/v1/', include(urls.router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
