import json

from django.db import models


class RemoteTorrent(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    name = models.TextField(null=False)
    upload_ratio = models.FloatField(null=False)
    download_dir = models.TextField(null=False)
    files = models.TextField(null=False)
    finished = models.BooleanField(null=False)

    @staticmethod
    def sync(client):
        RemoteTorrent.objects.all().delete()
        for torrent in client.get_torrents():
            files = [it for it in torrent.files().values() if it["selected"]]
            finished = any(it['completed'] != it['size'] for it in files)

            RemoteTorrent(id=torrent.hashString,
                          name=torrent.name,
                          upload_ratio=torrent.uploadRatio,
                          download_dir=torrent.downloadDir,
                          files=json.dumps([it["name"] for it in files], ensure_ascii=False),
                          finished=finished).save()


class Torrent(models.Model):
    name = models.TextField()
