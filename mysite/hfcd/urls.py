from django.conf.urls import url

from mysite.hfcd.views import *


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
    url(r'^help/step01/$', step01, name='step01'),
    url(r'^help/docs/the_story/$', the_story, name='the_story'),
    url(r'^help/docs/definitions/$', definitions, name='definitions'),
    url(r'^help/docs/$', help_docs, name='help_docs'),
    url(r'^help/step01a/$', step01a, name='step01a'),
    url(r'^rs_hospital/step02/$', step02, name='step02'),
    url(r'^rs_hospital/step02a/$', step02a, name='step02a'),
    url(r'^help/step03/$', step03, name='step03'),
    url(r'^rs_hospital/step03a/$', step03a, name='step03a'),
    url(r'^rs_hospital/step03b/$', step03b, name='step03b'),
]
