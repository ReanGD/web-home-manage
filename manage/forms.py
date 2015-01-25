# -*- coding: utf-8 -*-

import re

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms import TextInput, Select, NumberInput
from django.forms.models import modelform_factory
from django_ajax.decorators import ajax

from manage.models import LocalStorage, RemoteStorage, StorageMap


def _text_input_widget(placeholder):
    return TextInput(attrs={'placeholder': placeholder,
                            'class': 'form-control'})


def _select_widget():
    return Select(attrs={'class': 'selectpicker form-control'})


def _number_widget(min_value, max_value, step):
    return NumberInput(attrs={'min': min_value,
                              'max': max_value,
                              'step': step,
                              'class': 'form-control'})


class MetaModel(object):
    def __init__(self, model):
        self.model = model
        self._re1 = re.compile('(.)([A-Z][a-z]+)')
        self._re2 = re.compile('([a-z0-9])([A-Z])')

    def header(self):
        tmp = self._re1.sub(r'\1 \2', self.model.__name__)
        return self._re2.sub(r'\1 \2', tmp)

    def header_list(self):
        return self.header() + ":"

    def header_add(self):
        return "Add " + self.header().lower()

    def header_edit(self):
        return "Edit " + self.header().lower()

    def header_delete(self):
        return "Delete " + self.header().lower()

    def url(self):
        tmp = self._re1.sub(r'\1_\2', self.model.__name__)
        return "manage:" + self._re2.sub(r'\1 \2', tmp).lower()

    def url_add(self):
        return self.url() + "_add"

    def url_edit(self):
        return self.url() + "_edit"

    def url_delete(self):
        return self.url() + "_delete"


def _view(request, model, tForm):
    class ViewItem:
        def __init__(self, url_edit, url_delete, data):
            self.url_edit = url_edit
            self.url_delete = url_delete
            self.data = data

    form = tForm()
    meta_model = MetaModel(model)

    items = []
    for it in model.objects.all():
        url_edit = reverse(meta_model.url_edit(), args=[it.id])
        url_delete = reverse(meta_model.url_delete(), args=[it.id])
        data = tuple(getattr(it, field) for field in form.fields.keys())
        items.append(ViewItem(url_edit, url_delete, data))

    params = {'items': items,
              'action_add': reverse(meta_model.url_add()),
              'labels': [it.label for it in form.fields.values()],
              'header': meta_model.header_list()}
    return render(request, 'manage/standart_view.html', params)


def _process(request, action, id, model, widgets):
    tForm = modelform_factory(model, widgets=widgets)
    meta_model = MetaModel(model)

    if action == 'list':
        return _view(request, model, tForm)

    if action == 'edit':
        inst = get_object_or_404(model, pk=id)
        action_url = reverse(meta_model.url_edit(), args=[id])
        header = meta_model.header_edit()
        action_btn = "Save"
    elif action == 'delete':
        inst = get_object_or_404(model, pk=id)
        action_url = reverse(meta_model.url_delete(), args=[id])
        header = meta_model.header_delete()
        action_btn = "Delete"
    else:
        inst = model()
        action_url = reverse(meta_model.url_add())
        header = meta_model.header_add()
        action_btn = "Save"

    if request.method == 'POST':
        if action == 'delete':
            inst.delete()
            return HttpResponseRedirect(reverse('manage:index'))
        form = tForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage:index'))
    else:
        form = tForm(instance=inst)
        if action == 'delete':
            for it in form.fields.values():
                it.widget.attrs['disabled'] = 'disabled'

    params = {'form': form,
              'action': action_url,
              'header': header,
              'action_btn': action_btn}
    return render(request, 'manage/form_edit_add.html', params)


@ajax
def local_storage(request, action, id=None):
    widgets = {
        'name': _text_input_widget('Films'),
        'path': _text_input_widget('Films')}
    return _process(request, action, id, LocalStorage, widgets)


@ajax
def remote_storage(request, action, id=None):
    widgets = {
        'path': _text_input_widget('Media/Films')}
    return _process(request, action, id, RemoteStorage, widgets)


@ajax
def storage_map(request, action, id=None):
    widgets = {'local_ptr': _select_widget(),
               'remote_ptr': _select_widget(),
               'min_ratio': _number_widget(0.0, 2.0, 0.1)}
    return _process(request, action, id, StorageMap, widgets)
