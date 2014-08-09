import doctest
from django.test import TestCase
from django.test.utils import override_settings
from static_site import rewriter
from static_site.rewriter import (ExtensionRewriter, RegexRewriter)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(rewriter))
    return tests

class ExtensionRewriterTest(TestCase):
    
    @override_settings(PAGE_EXTENSION='.html')
    def test_rewrite(self):
        pass
