from django.db import models


class BindSettings(models.Model):
    remote = models.CharField(max_length=255, unique=True)
    local = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return "%s:%s" % (self.remote, self.local)


class Torrents(models.Model):
    idhash = models.CharField(max_length=40, unique=True, db_index=True)
    name = models.TextField(unique=False)

    def __unicode__(self):
        return "%s(%s)" % (self.name, self.idhash)


class TorrentFiles(models.Model):
    entity_ptr = models.ForeignKey(Torrents)
    path = models.TextField(unique=False)

    def __unicode__(self):
        return "%s: %s" % (self.job_ptr.name, self.name)
