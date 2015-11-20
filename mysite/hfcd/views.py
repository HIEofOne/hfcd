import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from mysite.hfcd.models import *


class HfcdViewsError(Exception):
    def __init__(self, description, more=''):
        self.description = description
        self.more = more
    def __str__(self):
        if self.more:
            return "%s:\n%s" % (self.description, self.more)
        else:
            return self.description


def welcome(request):
    return render(request, 'hfcd/welcome.html', {
        'user': request.user,
    })


def example_view(request):
    return render(request, 'hfcd/example_view.html', {
        'user': request.user,
        'page_title': "This Is the Page Title",
        'some_variable': 5.71,
    })


def raise_an_exception(request):
    raise HfcdViewsError("This is the description.", "This is more.")
