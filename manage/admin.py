from django.contrib import admin
from manage.models import BindSettings, Torrents, TorrentFiles

admin.site.register(BindSettings)
admin.site.register(Torrents)
admin.site.register(TorrentFiles)
