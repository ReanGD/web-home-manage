from rest_framework import serializers
from torrents.models import Remote, Local


class RemoteSerializer(serializers.ModelSerializer):
    local = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)

    class Meta:
        model = Remote
        fields = ('id', 'name', 'content_type', 'ratio', 'finished', 'dir', 'files', 'local')


class RemoteShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remote
        fields = ('name', 'content_type', 'dir', 'files')


class LocalSerializer(serializers.ModelSerializer):
    remote = RemoteShortSerializer(source='id', read_only=True)

    class Meta:
        model = Local
        fields = ('id', 'remote')

    def create(self, validated_data):
        id = validated_data['id']
        remote = Remote.objects.get(id=id)
        return Local.objects.create(id=remote)
