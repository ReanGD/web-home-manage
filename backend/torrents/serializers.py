from rest_framework import serializers
import torrents.models


class RemoteTorrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = torrents.models.RemoteTorrent
        fields = ('id', 'name', 'ratio', 'finished', 'dir', 'files')


class TorrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = torrents.models.Torrent
        fields = ('id', 'name')
