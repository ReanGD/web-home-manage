import os
import shutil
import traceback

from django.conf import settings
from torrents.models import Local, Remote


def _remove_local_torrent(torrent_id):
    remote = Remote.objects.get(id=torrent_id)
    print('Remove torrent "%s"' % remote.name)

    local_root = os.path.join(settings.TORRENT['ROOT']['LOCAL'], remote.dir)
    for it in remote.files:
        path = os.path.abspath(os.path.join(local_root, it['name']))

        if os.path.isfile(path):
            print('Remove file "%s"' % path)
            os.remove(path)

    Local.objects.filter(id=torrent_id).delete()


def remove_local_torrent(torrent_id):
    try:
        _remove_local_torrent(torrent_id)
    except Exception:
        print(traceback.format_exc())


def _create_local_torrent(torrent_id):
    remote = Remote.objects.get(id=torrent_id)
    print('Copy torrent "%s"' % remote.name)

    remote_root = os.path.join(settings.TORRENT['ROOT']['REMOTE'], remote.dir)
    local_root = os.path.join(settings.TORRENT['ROOT']['LOCAL'], remote.dir)

    for it in remote.files:
        from_path = os.path.abspath(os.path.join(remote_root, it['name']))
        to_path = os.path.abspath(os.path.join(local_root, it['name']))

        if not os.path.isfile(from_path):
            raise RuntimeError('can\'t find path %s' % from_path)

        if os.path.isfile(to_path):
            print('Remove old file from "%s"' % to_path)
            os.remove(to_path)

        print('Copy file from "%s" to "%s"' % (from_path, to_path))
        os.makedirs(os.path.dirname(to_path), exist_ok=True)
        shutil.copy2(from_path, to_path)

    Local.objects.filter(id=torrent_id).update(task_id='')


def create_local_torrent(torrent_id):
    try:
        _create_local_torrent(torrent_id)
    except Exception:
        print(traceback.format_exc())
        remove_local_torrent(torrent_id)
