#!/usr/bin/env python
import os, sys

def runtests(): 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    sys.path.insert(0, test_dir)
    
    import django
    if django.VERSION >= (1, 7):
        django.setup()
    
    from django.conf import settings
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['static_site'])
    sys.exit(bool(failures))
    
if __name__ == '__main__':
    runtests()
