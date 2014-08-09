import os
from django.conf import settings
from static_site.settings import default
prefix = 'STATIC_SITE_'

def get_settings(name):
    specify_name = prefix.join(name)
    if hasattr(settings, specify_name):
        return getattr(settings, specify_name)
    if hasattr(settings, name):
        return getattr(settings, name)
    if hasattr(default, name):
        return getattr(default, name)
    raise ValueError('{0} is a invalid settings name'.format(name))
