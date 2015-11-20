from django.conf.urls import url

from mysite.hfcd.views import *


urlpatterns = [
    url(r'^$', welcome, name='welcome'),
    url(r'^example_view/$', example_view, name='example_view'),
    url(r'^raise_an_exception/$', raise_an_exception, 
        name='raise_an_exception'),
]
