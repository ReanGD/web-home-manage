import json
import os

from django.db import models


class RemoteTorrent(models.Model):
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
        contents = {'Films': '/Media/Films',
                    'AudioBooks': '/Media/AudioBooks',
                    'Serials': '/Media/Serials'}

        for key, val in contents.items():
            if self.dir.startswith(val):
                return key

        return 'Others'


    @staticmethod
    def sync(client):
        base_dir = '/mnt/md1'
        RemoteTorrent.objects.all().delete()
        for torrent in client.get_torrents():
            files = [it for it in torrent.files().values() if it["selected"]]
            finished = not any(it['completed'] != it['size'] for it in files)
            dir = os.path.abspath(torrent.downloadDir)
            if dir.startswith('/mnt/md1/'):
                dir = dir[len(base_dir):]
            else:
                raise RuntimeError('Unknown base directory for "{}"'.format(dir))


            RemoteTorrent(id=torrent.hashString,
                          name=torrent.name,
                          ratio=round(torrent.uploadRatio, 1),
                          dir=dir,
                          files=[{'file': it["name"]} for it in files],
                          finished=finished).save()


class Torrent(models.Model):
    name = models.TextField()
