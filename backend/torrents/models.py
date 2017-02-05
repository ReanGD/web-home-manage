import json
import os

from django.db import models
from django.conf import settings


class Remote(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    name = models.TextField(null=False)
    ratio = models.FloatField(null=False)
    finished = models.BooleanField(null=False)
    dir = models.TextField(null=False)
    raw_files = models.TextField(null=False)

    @property
    def files(self):
        return json.loads(self.raw_files, encoding='utf-8')

    @files.setter
    def files(self, x):
        self.raw_files = json.dumps(x, ensure_ascii=False)

    @property
    def content_type(self):
        for key, val in settings.TORRENT['CONTENT_MAP'].items():
            if self.dir.startswith(val):
                return key

        return 'Others'

    @staticmethod
    def _update_or_create(torrent, db_torrent):
        base_dir = settings.TORRENT['BASE_REMOTE']
        raw_files = [it for it in torrent.files().values() if it["selected"]]
        finished = not any(it['completed'] != it['size'] for it in raw_files)
        dir = os.path.abspath(torrent.downloadDir)
        if dir.startswith(base_dir):
            dir = dir[len(base_dir):]
        else:
            raise RuntimeError('Unknown base directory for "{}"'.format(dir))
        ratio = round(torrent.uploadRatio, 1)
        files = [{'file': it["name"]} for it in raw_files]

        if db_torrent is None:
            Remote.objects.create(id=torrent.hashString,
                                  name=torrent.name,
                                  ratio=ratio,
                                  dir=dir,
                                  files=files,
                                  finished=finished)
        else:
            db_torrent.name = torrent.name
            db_torrent.ratio = ratio
            db_torrent.dir = dir
            db_torrent.files = files
            db_torrent.finished = finished
            db_torrent.save()

    @staticmethod
    def sync(client):
        remote_torrents = {it.hashString: it for it in client.get_torrents()}
        db_torrents = {it.id: it for it in Remote.objects.all()}

        for key, torrent in db_torrents.items():
            if key in remote_torrents.keys():
                Remote._update_or_create(remote_torrents[key], torrent)
            else:
                torrent.delete()

        for key, torrent in remote_torrents.items():
            if key not in db_torrents.keys():
                Remote._update_or_create(torrent, None)


class Local(models.Model):
    id = models.OneToOneField(Remote, related_name='local', primary_key=True)
    task_id = models.CharField(max_length=40, null=True)
