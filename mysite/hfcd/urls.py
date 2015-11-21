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
]
