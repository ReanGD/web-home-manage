import os
import shutil


def copy_file(from_path, to_path):
    if not os.path.isfile(from_path):
        raise RuntimeError('can\'t find path %s' % from_path)

    if os.path.isfile(to_path):
        os.remove(to_path)

    os.makedirs(os.path.dirname(to_path), exist_ok=True)
    shutil.copy2(from_path, to_path)
