import time
import transmissionrpc
from rest_framework import mixins
from rest_framework import viewsets
from torrents.models import RemoteTorrent, LocalTorrent
from torrents.serializers import RemoteTorrentSerializer, LocalTorrentSerializer


class RemoteTorrentList(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    queryset = RemoteTorrent.objects.all()
    serializer_class = RemoteTorrentSerializer
    _cache_expired = time.time()

    def dispatch(self, *args, **kwargs):
        if time.time() > RemoteTorrentList._cache_expired:
            client = transmissionrpc.Client('192.168.1.8', 9091, 'admin', 'admin')
            RemoteTorrent.sync(client)
            RemoteTorrentList._cache_expired = time.time() + 5 * 60

        return super(RemoteTorrentList, self).dispatch(*args, **kwargs)

class LocalTorrentList(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    pagination_class = None
    queryset = LocalTorrent.objects.all()
    serializer_class = LocalTorrentSerializer
