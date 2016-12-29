import json

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

    @staticmethod
    def sync(client):
        RemoteTorrent.objects.all().delete()
        for torrent in client.get_torrents():
            files = [it for it in torrent.files().values() if it["selected"]]
            finished = not any(it['completed'] != it['size'] for it in files)

            RemoteTorrent(id=torrent.hashString,
                          name=torrent.name,
                          ratio=torrent.uploadRatio,
                          dir=torrent.downloadDir,
                          files=json.dumps([it["name"] for it in files], ensure_ascii=False),
                          finished=finished).save()


class Torrent(models.Model):
    name = models.TextField()
