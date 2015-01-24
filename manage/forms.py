# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms import TextInput
from django.forms.models import modelform_factory

from manage.models import LocalStorage, RemoteStorage


def _text_input_widget(placeholder):
    return TextInput(attrs={'placeholder': placeholder,
                            'class': 'form-control'})


def local_storage(request, id=None):
    if id:
        inst = get_object_or_404(LocalStorage, pk=id)
        action = reverse('manage:form_local_storage', args=[id])
    else:
        inst = LocalStorage()
        action = reverse('manage:form_local_storage')

    tForm = modelform_factory(LocalStorage, widgets={
        'name': _text_input_widget('Films'),
        'path': _text_input_widget('Films')})

    if request.method == 'POST':
        form = tForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage:index'))
    else:
        form = tForm(instance=inst)

    return render(request, 'manage/form_local_storage.html',
                  {'form': form, 'action': action})


def remote_storage(request, id=None):
    if id:
        inst = get_object_or_404(RemoteStorage, pk=id)
        action = reverse('manage:form_remote_storage', args=[id])
    else:
        inst = RemoteStorage()
        action = reverse('manage:form_remote_storage')

    tForm = modelform_factory(RemoteStorage, widgets={
        'path': _text_input_widget('Media/Films')})

    if request.method == 'POST':
        form = tForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage:index'))
    else:
        form = tForm(instance=inst)

    return render(request, 'manage/form_remote_storage.html',
                  {'form': form, 'action': action})


def save_storage_map(request):
    # settings.set_jenkins_url(request.POST['JenkinsUrl'])
    return HttpResponseRedirect(reverse('manage:index'))
