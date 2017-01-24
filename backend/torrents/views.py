import time
import transmissionrpc
from rest_framework import mixins
from rest_framework import viewsets
from torrents.models import Remote, Local
from torrents.serializers import RemoteSerializer, LocalSerializer


class RemoteList(mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pagination_class = None
    queryset = Remote.objects.all()
    serializer_class = RemoteSerializer
    _cache_expired = time.time()

    def dispatch(self, *args, **kwargs):
        if time.time() > RemoteList._cache_expired:
            client = transmissionrpc.Client('192.168.1.8', 9091, 'admin', 'admin')
            Remote.sync(client)
            RemoteList._cache_expired = time.time() + 5 * 60

        return super(RemoteList, self).dispatch(*args, **kwargs)


class LocalList(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pagination_class = None
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
