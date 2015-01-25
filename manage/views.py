# -*- coding: utf-8 -*-

from django_ajax.decorators import ajax
from django.shortcuts import render


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
