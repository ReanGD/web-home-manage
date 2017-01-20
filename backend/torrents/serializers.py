from rest_framework import serializers
from torrents.models import RemoteTorrent, LocalTorrent


class RemoteTorrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteTorrent
        fields = ('id', 'name', 'content_type', 'ratio', 'finished', 'dir', 'files')


class LocalTorrentSerializer(serializers.ModelSerializer):
    remote = RemoteTorrentSerializer(source='id', read_only=True)

    class Meta:
        model = LocalTorrent
        fields = ('id', 'remote')

    def create(self, validated_data):
        id = validated_data['id']
        remote = RemoteTorrent.objects.get(id=id)
        return LocalTorrent.objects.create(id=remote)
