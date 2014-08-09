from django.conf.urls import patterns, include, url

import static_site.urls

urlpatterns = patterns('',
    url('', include(static_site.urls)),
)
