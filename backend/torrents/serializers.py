from rest_framework import serializers
from torrents.models import Remote, Local


class RemoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remote
        fields = ('id', 'name', 'content_type', 'ratio', 'finished', 'dir', 'files')


class LocalSerializer(serializers.ModelSerializer):
    remote = RemoteSerializer(source='id', read_only=True)

    class Meta:
        model = Local
        fields = ('id', 'remote')

    def create(self, validated_data):
        id = validated_data['id']
        remote = Remote.objects.get(id=id)
        return Local.objects.create(id=remote)
