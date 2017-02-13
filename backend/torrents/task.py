import os
import traceback

from django.conf import settings
from torrents.models import Local, Remote
from torrents.utils import copy_file


def create_local_torrent(torrent_id):
    try:
        remote = Remote.objects.get(id=torrent_id)

        remote_root = os.path.join(settings.TORRENT['ROOT']['REMOTE'], remote.dir)
        local_root = os.path.join(settings.TORRENT['ROOT']['LOCAL'], remote.dir)

        for it in remote.files:
            from_path = os.path.abspath(os.path.join(remote_root, it['file']))
            to_path = os.path.abspath(os.path.join(local_root, it['file']))
            print('Copy file from "%s" to "%s"' % (from_path, to_path))
            copy_file(from_path, to_path)

        Local.objects.filter(id=torrent_id).update(task_id='')
    except Exception:
        print(traceback.format_exc())
        Local.objects.filter(id=torrent_id).delete()
