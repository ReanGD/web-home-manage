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
    local_ptr = models.ForeignKey(LocalStorage, verbose_name="Local")
    remote_ptr = models.ForeignKey(RemoteStorage, verbose_name="Remote")
    min_ratio = models.FloatField(null=False, default=2.0)

    class Meta:
        unique_together = (("local_ptr", "remote_ptr"),)

    def __unicode__(self):
        msg = "%s <==> %s: min rating: %f"
        return msg % (self.local_ptr,
                      self.remote_ptr,
                      self.min_ratio)


class Torrent(models.Model):
    storage_map_ptr = models.ForeignKey(LocalStorage,
                                        verbose_name="Storage map")
    name = models.TextField(unique=False)
    idhash = models.CharField("Hash", max_length=40, unique=True, db_index=True)

    def __unicode__(self):
        return "%s: %s(%s)" % (self.storage_map_ptr, self.name, self.idhash)


class TorrentFile(models.Model):
    torent_ptr = models.ForeignKey(Torrent, verbose_name="Torrent")
    path = models.TextField(unique=False)

    def __unicode__(self):
        return "%s: %s" % (self.torent_ptr.name, self.path)
