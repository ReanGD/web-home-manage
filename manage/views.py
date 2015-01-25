# -*- coding: utf-8 -*-

from django_ajax.decorators import ajax
from django.shortcuts import render
from django.core.urlresolvers import reverse
from manage.models import LocalStorage, RemoteStorage, StorageMap


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


def _generate_view(request, tModel, form_url, header):
    class ViewItem:
        def __init__(self, url, data):
            self.url = url
            self.data = data

    items = []
    for it in tModel.objects.all():
        url = reverse(form_url, args=[it.id])
        items.append(ViewItem(url, it.default_view()))

    params = {'items': items,
              'action_add': reverse(form_url),
              'captions': tModel.default_captions(),
              'header': header}
    return render(request, 'manage/standart_view.html', params)


@ajax
def local_storage(request):
    return _generate_view(request,
                          LocalStorage,
                          "manage:form_local_storage",
                          "Local storage:")


@ajax
def remote_storage(request):
    return _generate_view(request,
                          RemoteStorage,
                          "manage:form_remote_storage",
                          "Remote storage:")


@ajax
def storage_map(request):
    return _generate_view(request,
                          StorageMap,
                          "manage:form_storage_map",
                          "Storage map:")
