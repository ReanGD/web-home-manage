from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from torrents import views

urlpatterns = [
    url(r'^torrents/$', views.RemoteTorrentList.as_view()),
    url(r'^torrents/$', views.TorrentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)