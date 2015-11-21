import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from mysite.hfcd.models import *
from mysite.view_helpers import multipurpose


class HfcdViewsError(Exception):
    def __init__(self, description, more=''):
        self.description = description
        self.more = more
    def __str__(self):
        if self.more:
            return "%s:\n%s" % (self.description, self.more)
        else:
            return self.description


class PageData(object):
    """Stores the header (top banner), server name, and your character
    
    Note that self.header appears in the top banner, but everything else appears in the right-hand sidebar (box).
    
    Iff you_are == None then you are not pretending to be anyone.
    
    """
    
    def __init__(self, header, server, owner, you_are, curr_step=None, 
                 total_steps=None, is_help=False):
        self.header = header    # Example: "Big Hospital"
        self.server = server    # Example: "Hospital EHR (RS)"
        self.owner = owner      # Example: "Big Hospital, Inc." or alice_str
        self.you_are = you_are  # Example: "Alice (the patient)"
        self.curr_step = curr_step
        self.total_steps = total_steps
        self.is_help = is_help  # Is this a meta / help page?


# These are the allowable values of PageData.you_are:
alice_str = "Alice (the patient, RO)"
bob_str = "Bob (the doctor, RqP)"


class HospitalPageData(PageData):
    """This is a PageData object with some defaults set"""
    
    def __init__(self, you_are, curr_step=None, total_steps=None):
        super(HospitalPageData, self).__init__(
            header = "Big Hospital",
            server = "Hospital EHR (RS)",
            owner = "Big Hospital, Inc.",
            you_are = you_are,
            curr_step = curr_step,
            total_steps = total_steps)

class AuthServerPageData(PageData):
    def __init__(self, you_are, curr_step=None, total_steps=None):
        super(AuthServerPageData, self).__init__(
            header = "Alice's HIE of One Server",
            server = "Authorization Server (AS)",
            owner = alice_str,
            you_are = you_are,
            curr_step = curr_step,
            total_steps = total_steps)

class BobServerPageData(PageData):
    def __init__(self, you_are, curr_step=None, total_steps=None):
        super(BobServerPageData, self).__init__(
            header = "Dr. Bob's Server",
            server = "Dr. Bob's Server (C)",
            owner = bob_str,
            you_are = you_are,
            curr_step = curr_step,
            total_steps = total_steps)

class HelpPageData(PageData):
    """This is used on /help/ pages, which give information"""
    
    def __init__(self, you_are, curr_step=None, total_steps=None):
        super(HelpPageData, self).__init__(
            header = "HIE of One Demo Help",
            server = "N/A",
            owner = "N/A",
            you_are = you_are,
            curr_step = curr_step,
            total_steps = total_steps,
            is_help = True)


def welcome(request):
    page_data = HelpPageData(you_are = None)
    return render(request, 'hfcd/welcome.html', {
        'user': request.user,
        'page_data': page_data,
    })


def example_view(request):
    return render(request, 'hfcd/example_view.html', {
        'user': request.user,
        'page_title': "This Is the Page Title",
        'some_variable': 5.71,
    })


def full_example(request):
    if False:
        page_data = PageData(
            header = "Big Hospital",
            server = "Hospital EHR (RS)",
            owner = "Big Hospital, Inc.",
            you_are = "Alice (the patient, RO)",
            curr_step = 2,
            total_steps = 3)
    
    elif False:
        # This should look exactly the same as the clause above:
        page_data = HospitalPageData(
            you_are = alice_str,
            curr_step = 2,
            total_steps = 3)
    
    elif True:
        page_data = HelpPageData(
            you_are = alice_str,
            curr_step = 2,
            total_steps = 3)
    
    return render(request, 'hfcd/full_example.html', {
        'user': request.user,
        'page_title': "Full Example page_title",
        'page_data': page_data,
    })


def raise_an_exception(request):
    raise HfcdViewsError("This is the description.", "This is more.")


def debugging_links(request):
    return render(request, 'hfcd/debugging_links.html', {
        'user': request.user,
        'page_title': "Debugging Links",
    })


def example_multipurpose(request):
    return multipurpose(
        request,
        "This Is the Title of a Multipurpose Page",
        subtitle = "<p>Includes <b>HTML.</b></p>",
        is_safe = True,
        show_back = True,
        show_reload = False)
