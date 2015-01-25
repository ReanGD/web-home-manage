# -*- coding: utf-8 -*-

from django_ajax.decorators import ajax
from django.shortcuts import render

from manage.models import StorageMap, Torrent


def index(request):
    items = StorageMap.objects.all()
    return render(request, 'manage/index.html', {'items': items})


@ajax
def torrent(request, id):
    storage_map = StorageMap.objects.get(pk=id)
    items = Torrent.objects.filter(storage_map_ptr=id)
    return render(request, 'manage/torrent_view.html',
                  {'items': items, 'header': storage_map.local_ptr.name})
