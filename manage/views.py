# -*- coding: utf-8 -*-

from django_ajax.decorators import ajax
from django.shortcuts import render
from manage.models import LocalStorage, RemoteStorage, StorageMap, Torrent, TorrentFile


def index(request):
    return render(request, 'manage/index.html')


@ajax
def get_films(request):
    class Film(object):
        def __init__(self, name):
            self.name = name

    items = [Film("one"), Film("two")]
    return render(request, 'manage/data_films.html', {'items': items})


@ajax
def get_audiobooks(request):
    class Book(object):
        def __init__(self, name):
            self.name = name

    items = [Book("first"), Book("second")]
    return render(request, 'manage/data_audiobooks.html', {'items': items})


@ajax
def local_storage(request):
    items = LocalStorage.objects.all()
    return render(request, 'manage/data_local_storage.html', {'items': items})


@ajax
def get_remote_storage(request):
    items = RemoteStorage.objects.all()
    return render(request, 'manage/data_remote_storage.html', {'items': items})


@ajax
def get_storage_map(request):
    items = StorageMap.objects.all()
    return render(request, 'manage/data_storage_map.html', {'items': items})
