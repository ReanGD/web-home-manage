import time
from torrents.models import Local


def create_local_torrent(torrent_id):
    local = Local.objects.get(id=torrent_id)
    time.sleep(30)
    local.task_id = ''
    local.save()
