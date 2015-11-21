from django.conf.urls import url

from mysite.hfcd.views import *


def help_url(vf, vf_name):
    return url(
        r'^help/%s/$' % vf_name,
        vf,
        name = vf_name)

def auth_server_url(vf, vf_name):
    return url(
        r'^as_auth_server/%s/$' % vf_name,
        vf,
        name = vf_name)

def bob_server_url(vf, vf_name):
    return url(
        r'^c_bob_server/%s/$' % vf_name,
        vf,
        name = vf_name)

def hospital_url(vf, vf_name):
    return url(
        r'^rs_hospital/%s/$' % vf_name,
        vf,
        name = vf_name)


urlpatterns = [
    url(r'^$', welcome, name='welcome'),
    url(r'^broken_link/$', broken_link, name='broken_link'),
    url(r'^example_view/$', example_view, name='example_view'),
    url(r'^raise_an_exception/$', raise_an_exception, 
        name='raise_an_exception'),
    url(r'^debugging_links/$', debugging_links, name='debugging_links'),
    url(r'^example_multipurpose/$', example_multipurpose, 
        name='example_multipurpose'),
    url(r'^full_example/$', full_example, name='full_example'),
    url(r'^help/docs/the_story/$', the_story, name='the_story'),
    url(r'^help/docs/definitions/$', definitions, name='definitions'),
    url(r'^help/docs/$', help_docs, name='help_docs'),
    
    ## The following URL patterns show how normal steps work, if hand-coded:
    # url(r'^help/step01/$', step01, name='step01'),
    # url(r'^help/step01a/$', step01a, name='step01a'),
    # url(r'^rs_hospital/step02/$', step02, name='step02'),
    # url(r'^rs_hospital/step02a/$', step02a, name='step02a'),
    # url(r'^help/step03/$', step03, name='step03'),
    # url(r'^rs_hospital/step03a/$', step03a, name='step03a'),
    # url(r'^rs_hospital/step03b/$', step03b, name='step03b'),
    
    # The following URLs use the convenience functions. Note that the top 7 
    # patterns are duplicates of the commented-out URL patterns above:
    help_url(step01, 'step01'),
    help_url(step01a, 'step01a'),
    hospital_url(step02, 'step02'),
    hospital_url(step02a, 'step02a'),
    help_url(step03, 'step03'),
    hospital_url(step03a, 'step03a'),
    hospital_url(step03b, 'step03b'),
    hospital_url(hospital_roi_form, 'hospital_roi_form'),
    help_url(step05, 'step05'),
    auth_server_url(step07, 'step07'),
    help_url(step08, 'step08'),
]
