from rest_framework import serializers
from torrents.models import Torrent


class TorrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torrent
        fields = ('id', 'name')
