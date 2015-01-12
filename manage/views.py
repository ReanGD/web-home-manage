# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect


def index(request):
    return redirect('/manage/films/')


def films(request):
    class Film(object):
        def __init__(self, name):
            self.name = name

    items = [Film("one"), Film("two")]
    return render(request, 'manage/films.html', {'items': items})


def audiobook(request):
    class Book(object):
        def __init__(self, name):
            self.name = name

    items = [Book("first"), Book("second")]
    return render(request, 'manage/audiobook.html', {'items': items})
