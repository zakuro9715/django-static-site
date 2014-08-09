from setuptools import setup, find_packages

setup(
    name = 'django-static-site',
    version = '1.0.0',
    description = 'static site generator for django',
    author = 'YuZakuro',
    author_email = 'zakuro@yuzakuro.me',
    url = 'http://github.com/zakuro9715/django-static-site',
    packages = [
        'static_site'
    ],
    test_suite = 'runtest'
)
