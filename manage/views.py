# -*- coding: utf-8 -*-

from django_ajax.decorators import ajax
from django.shortcuts import render

from manage.models import StorageMap, Torrent


def index(request):
    items = StorageMap.objects.all()
    tabid = request.session.get('tabid', None)
    if tabid is None:
        tabid = "id_%i" % items[0].id
    return render(request, 'manage/index.html',
                  {'items': items, 'load_tab': tabid})


@ajax
def torrent(request, id):
    storage_map = StorageMap.objects.get(pk=id)
    items = Torrent.objects.filter(storage_map_ptr=id)
    header = storage_map.local_ptr.name + ":"
    request.session['tabid'] = "id_%i" % storage_map.id
    return render(request, 'manage/torrent_view.html',
                  {'items': items, 'header': header})
