from django_q.tasks import async
from rest_framework import serializers
from torrents.models import Remote, Local


class RemoteSerializer(serializers.ModelSerializer):
    local = serializers.SlugRelatedField(many=False,
                                         read_only=True,
                                         allow_null=True,
                                         slug_field='task_id')

    class Meta:
        model = Remote
        fields = ('id', 'name', 'content_type', 'ratio', 'finished', 'dir', 'files', 'size', 'local')


class RemoteShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remote
        fields = ('name', 'content_type', 'dir', 'size', 'files')


class LocalSerializer(serializers.ModelSerializer):
    remote = RemoteShortSerializer(source='id', read_only=True)

    class Meta:
        model = Local
        fields = ('id', 'remote', 'task_id')

    def create(self, validated_data):
        torrent_id = validated_data['id']
        remote = Remote.objects.get(id=torrent_id)
        local = Local.objects.create(id=remote)
        local.task_id = async('torrents.task.create_local_torrent',
                              torrent_id, task_name='copy '+remote.name)
        local.save()
        return local
