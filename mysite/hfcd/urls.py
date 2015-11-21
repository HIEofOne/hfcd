from django.conf.urls import url

from mysite.hfcd.views import *


urlpatterns = [
    url(r'^$', welcome, name='welcome'),
    url(r'^example_view/$', example_view, name='example_view'),
    url(r'^raise_an_exception/$', raise_an_exception, 
        name='raise_an_exception'),
    url(r'^debugging_links/$', debugging_links, name='debugging_links'),
    url(r'^example_multipurpose/$', example_multipurpose, 
        name='example_multipurpose'),
    url(r'^full_example/$', full_example, name='full_example'),
]
