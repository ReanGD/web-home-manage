# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms import TextInput, Select, NumberInput
from django.forms.models import modelform_factory

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


def _form_process(request, id, tModel, widgets, form_url, header, labels={}):
    if id:
        inst = get_object_or_404(tModel, pk=id)
        action = reverse(form_url, args=[id])
    else:
        inst = tModel()
        action = reverse(form_url)

    tForm = modelform_factory(tModel, widgets=widgets, labels=labels)

    if request.method == 'POST':
        form = tForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage:index'))
    else:
        form = tForm(instance=inst)

    return render(request, 'manage/form_edit_add.html',
                  {'form': form, 'action': action, 'header': header})


def local_storage(request, id=None):
    url = 'manage:form_local_storage'
    if id:
        header = "Edit local storage"
    else:
        header = "Add local storage"
    widgets = {
        'name': _text_input_widget('Films'),
        'path': _text_input_widget('Films')}

    return _form_process(request, id, LocalStorage, widgets, url, header)


def remote_storage(request, id=None):
    url = 'manage:form_remote_storage'
    if id:
        header = "Edit remote storage"
    else:
        header = "Add remote storage"
    widgets = {
        'path': _text_input_widget('Media/Films')}

    return _form_process(request, id, RemoteStorage, widgets, url, header)


def storage_map(request, id=None):
    url = 'manage:form_storage_map'
    if id:
        header = "Edit storage map"
    else:
        header = "Add storage map"
    widgets = {'local_ptr': _select_widget(),
               'remote_ptr': _select_widget(),
               'min_ratio': _number_widget(0.0, 2.0, 0.1)}
    labels = {'local_ptr': 'Local',
              'remote_ptr': 'Remote',
              'min_ratio': 'Min ratio'}

    return _form_process(request, id, StorageMap, widgets, url, header, labels)
