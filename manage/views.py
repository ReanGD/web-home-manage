# -*- coding: utf-8 -*-

from django_ajax.decorators import ajax
from django.shortcuts import render, get_object_or_404

from manage.models import StorageMap, Torrent, TorrentFile


def index(request):
    items = StorageMap.objects.all()
    tabid = request.session.get('tabid', None)
    if tabid is None:
        if len(items) == 0:
            tabid = "id_local_storage"
        else:
            tabid = "id_%i" % items[0].id
    return render(request, 'manage/index.html',
                  {'items': items, 'load_tab': tabid})


@ajax
def torrent(request, id):
    storage_map = get_object_or_404(StorageMap, pk=id)
    header = storage_map.local_ptr.name + ":"
    request.session['tabid'] = "id_%i" % storage_map.id

    items = Torrent.objects.filter(storage_map_ptr=id)
    for it in items:
        it.files = TorrentFile.objects.filter(torent_ptr=it)

    return render(request, 'manage/torrent_view.html',
                  {'items': items, 'header': header})
