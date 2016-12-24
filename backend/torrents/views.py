from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from torrents.models import Torrent
from rest_framework import viewsets
from torrents.serializers import TorrentSerializer
import transmissionrpc

class TorrentList(viewsets.ModelViewSet):
    # class TorrentList(APIView):
    queryset = Torrent.objects.all()
    serializer_class = TorrentSerializer

    # def get(self, request, format=None):
    #     snippets = Torrent.objects.all()
    #     serializer = TorrentSerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = TorrentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)