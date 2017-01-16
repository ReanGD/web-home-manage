import time
import transmissionrpc
from rest_framework import viewsets
from torrents.models import RemoteTorrent, Torrent
from torrents.serializers import RemoteTorrentSerializer, TorrentSerializer


class RemoteTorrentList(viewsets.ReadOnlyModelViewSet):
    queryset = RemoteTorrent.objects.all()
    serializer_class = RemoteTorrentSerializer
    _cache_expired = time.time()

    def dispatch(self, *args, **kwargs):
        if time.time() > RemoteTorrentList._cache_expired:
            client = transmissionrpc.Client('192.168.1.8', 9091, 'admin', 'admin')
            RemoteTorrent.sync(client)
            RemoteTorrentList._cache_expired = time.time() + 5 * 60

        return super(RemoteTorrentList, self).dispatch(*args, **kwargs)


class TorrentList(viewsets.ModelViewSet):
    queryset = Torrent.objects.all()
    serializer_class = TorrentSerializer
