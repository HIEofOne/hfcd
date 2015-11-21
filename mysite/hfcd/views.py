import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from mysite.hfcd.models import *
from mysite.view_helpers import multipurpose


NUM_STEPS = 22


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
    page_data.header = "HIE of One Demo"
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


def broken_link(request):
    return multipurpose(
        request,
        "Broken Link",
        subtitle = "This website is incomplete.",
        show_back = True)


def help_docs(request):
    """List the help pages"""
    
    page_data = HelpPageData(None)
    page_title = "Documentation Home (Help)"
    
    help_pages = [
        ('the_story', "The Demo Story"),
        ('definitions', "Defintions"),
    ]
    
    return render(request, 'hfcd/help_docs.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'help_pages': help_pages,
    })


def the_story(request):
    """This page explains the Demo Story"""
    
    page_data = HelpPageData(None)
    page_title = "The Demo Story"
    
    return render(request, 'hfcd/the_story.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
    })


def definitions(request):
    """This page has helpful definitions"""
    
    page_data = HelpPageData(None)
    page_title = "Helpful Definitions"
    
    terms = [
        ('Alice', 
         "Alice is the patient. She is also the Resource Owner or RO."),
        ('Bob', 
         "Bob is the doctor. He is also the Requesting Party or RqP."),
        ('Big Hospital', 
         "This is the hospital. They are the Resource Server or RS. They are also a non-person entity (NPE). The hospital has an electronic health record system (EHR). In some documents, the hospital's EHR is called EHR-B. Sometimes the hospital's EHR is called the NPE EHR. The 'other' EHR is Dr. Bob's EHR. For information about Dr. Bob's EHR, see RqP and C (client)."),
        ('C', 
         "This stands for Client. The client, in this context, is Dr. Bob's EHR. Recall that Dr. Bob is the Requesting Party or RqP. Bob's EHR is sometimes called EHR-A."),
        ('RO', "Resource Owner, Alice, the patient."),
        ('RS', 
         "Resource Server, this is the Big Hospital EHR. This server has Alice's blood test results. Notice that Alice's server never has the blood test results, Alice's server only handles authorization."),
        ('AS', 
         "Authorization Server, this is Alice's server. This is an HIE of One server. Alice owns and controls this server."),
        ('RqP', 
         "Requesting Party, this is Dr. Bob, he requests the blood test results from the hospital."),
        ('Principal', 
         "This is Alice (the patient, the Resource Owner, the RO)."),
        ('NPE', 
         "Non-person entity. In some contexts, this refers specifically to the Big Hospital (the Resource Server, the RS)."),
    ]
    
    terms.sort(key=lambda term: term[0])
    
    return render(request, 'hfcd/definitions.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'terms': terms,
    })


#=========================== The Steps of the Story ===========================#

def example_step(request):
    """Copy-paste this and then change it"""
    
    page_data = TodoPageData(XXyou_are, XXcurr_step, NUM_STEPS)
    page_title = "Window Title and H1 Header"
    next_step = 'broken_link'
    
    page_content = """
    <p>
        Lorem ipsum.
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step01(request):
    """This is the first step of the Demo Story"""
    
    page_data = HelpPageData(None, 1, NUM_STEPS)
    page_title = "Step 1: The Beginning"
    next_step = 'step01a'
    
    page_content = """
    <p>
        Alice is a normal person, she is not very tech-savvy. A few months ago, Alice set up an 
        <a href="http://hieofone.org/">HIE of One</a>
        server. It was easy, the setup process only required a credit card and an email address and/or phone number (for SMS messages). Alice's server is an Authorization Server (AS), and she can use it to grant other people access to her medical records.
    </p>
    
    <p>
        Today, Alice is going to the hospital for blood tests. She wants to share her blood test results with her doctor, Bob, but he is not affiliated with the hospital.
    </p>
    
    <p>
        Starting now, you will be impersonating Alice.
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step01a(request):
    page_data = HelpPageData(alice_str, 1, NUM_STEPS)
    page_title = "Alice at the Hospital"
    next_step = 'step02'
    
    page_content = """
    <p>
        You (Alice) go to the hospital and get your blood drawn. The hospital analyzes your blood and stores the results in an electronic health record (EHR) on a server owned by the hospital.
    </p>
    
    <p>
        The hospital has a website, a patient gateway. This website allows you to access your own health records. In order to access your health records, you will need a password.
    </p>
    
    <p>
        In order to get a password for the hospital patient gateway, you go to the receptionist and show your driver's license to identify yourself. Now that the hospital has verified your identity, they will allow you to create a password.
    </p>
    
    <p>
        The receptionist hands you an iPad.
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step02(request):    
    page_data = HospitalPageData(alice_str, 2, NUM_STEPS)
    page_title = "Choose a Password for the Patient Gateway"
    next_step = 'step02a'
    
    page_content = """
    <p>
        Hello Alice. Please choose a password and enter it below. After you go home, you can use this password to login and view your hospital records.
    </p>
    
    <p>
        New Password:
        <input type="password" size="20" />
        (Demo note: Your input will be ignored.)
        
        <br /><br />
        
        Repeat Password:
        <input type="password" size="20" />
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step02a(request):    
    page_data = HospitalPageData(alice_str, 2, NUM_STEPS)
    page_title = "Thank You for Choosing a Password"
    next_step = 'step03'
    
    page_content = """
    <p>
        Your password has been saved.
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step03(request):
    page_data = HelpPageData(alice_str, 3, NUM_STEPS)
    page_title = "Alice Goes Home"
    next_step = 'step03a'
    
    page_content = """
    <p>
        Having created a password, you drive home. Once at home, you open your laptop and you go to BigHospital.com to access your medical records.
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step03a(request):    
    page_data = HospitalPageData(alice_str, 3, NUM_STEPS)
    page_title = "Enter Your Patient Gateway Password"
    next_step = 'step03b'
    
    page_content = """
    <p>
        Welcome to the Big Hospital website. You can use this website to access or share your medical records.
    </p>
    
    <p>
        Username:
        <input type="text" value="Alice" size="30" />
        
        <br /><br />
        
        Password:
        <input type="password" size="20" />
        (Demo note: You can type anything.)
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })


def step03b(request):    
    page_data = HospitalPageData(alice_str, 3, NUM_STEPS)
    page_title = "Thank You for Logging In"
    next_step = 'broken_link'
    
    page_content = """
    <p>
        Thank you for logging in.
    </p>
    """
    
    return render(request, 'hfcd/normal_step.html', {
        'user': request.user,
        'page_title': page_title,
        'page_data': page_data,
        'page_content': page_content,
        'next_step': next_step,
    })
