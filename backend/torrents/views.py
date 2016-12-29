from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_swagger import renderers
from torrents.models import RemoteTorrent, Torrent
from torrents.serializers import RemoteTorrentSerializer, TorrentSerializer


# class RemoteTorrentList(APIView, GenericAPIView):
#     def get(self, request, format=None):
#         RemoteTorrent.sync()
#         remote_torrents = RemoteTorrent.objects.all()
#         serializer = RemoteTorrentSerializer(remote_torrents, many=True)
#         return Response(serializer.data)
class RemoteTorrentList(viewsets.ReadOnlyModelViewSet):
    queryset = RemoteTorrent.objects.all()
    serializer_class = RemoteTorrentSerializer


class TorrentList(viewsets.ModelViewSet):
    queryset = Torrent.objects.all()
    serializer_class = TorrentSerializer
