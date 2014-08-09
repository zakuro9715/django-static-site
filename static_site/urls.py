from django.conf.urls import patterns, url

urlpatterns = patterns('static_site.views',
    url(r'^(?P<path>.*)$', 'page'),
)
