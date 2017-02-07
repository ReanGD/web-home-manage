import time
import transmissionrpc
from django.conf import settings
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.response import Response

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
            st = settings.TORRENT['TRANSMISSION']
            client = transmissionrpc.Client(st['HOST'], st['PORT'], st['USER'], st['PASS'])
            Remote.sync(client)
            RemoteList._cache_expired = time.time() + st['UPDATE_TIMEOUT_SEC']

        return super(RemoteList, self).dispatch(*args, **kwargs)


class LocalList(mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pagination_class = None
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

