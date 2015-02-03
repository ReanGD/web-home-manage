from manage.models import LoadLog


class DbLogger(object):
    def __init__(self, rec_id=None):
        if rec_id is None:
            self.rec = LoadLog.objects.create()
        else:
            self.rec = LoadLog.objects.get(pk=int(rec_id))

    def id(self):
        return self.rec.id

    def text(self):
        return self.rec.text

    def write(self, msg):
        self.rec.text += ("\n" + msg)
        self.rec.save()

    def set_result(self, result):
        self.rec.result = result
        self.rec.save()

    def set_torrent(self, t):
        self.torent_ptr = t
        self.rec.save()
