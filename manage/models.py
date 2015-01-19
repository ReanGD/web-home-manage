from django.db import models


class LocalStorage(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    path = models.CharField(max_length=255, unique=True, null=False)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.path)


class RemoteStorage(models.Model):
    path = models.CharField(max_length=255, unique=True, null=False)

    def __unicode__(self):
        return "%s" % self.path


class StorageMap(models.Model):
    local_ptr = models.ForeignKey(LocalStorage)
    remote_ptr = models.ForeignKey(RemoteStorage)
    min_ratio = models.FloatField(null=False, default=2.0)

    def __unicode__(self):
        msg = "%s (%s) <==> %s: min rating: %f"
        return msg % (self.local_ptr.name,
                      self.local_ptr.path,
                      self.remote_ptr.path,
                      self.min_ratio)


class Torrent(models.Model):
    storage_ptr = models.ForeignKey(LocalStorage)
    name = models.TextField(unique=False)
    idhash = models.CharField(max_length=40, unique=True, db_index=True)

    def __unicode__(self):
        return "%s: %s(%s)" % (self.storage_ptr.name, self.name, self.idhash)


class TorrentFile(models.Model):
    torent_ptr = models.ForeignKey(Torrent)
    path = models.TextField(unique=False)

    def __unicode__(self):
        return "%s: %s" % (self.job_ptr.name, self.name)
