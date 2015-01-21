# -*- coding: utf-8 -*-

# from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# from fitnesse.models import Job

# import fitnesse.helper.settings as settings


def save_local_storage(request):
    # settings.set_jenkins_url(request.POST['JenkinsUrl'])
    return HttpResponseRedirect(reverse('manage:index'))


def save_remote_storage(request):
    # settings.set_jenkins_url(request.POST['JenkinsUrl'])
    return HttpResponseRedirect(reverse('manage:index'))
