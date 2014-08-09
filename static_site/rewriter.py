import re
import os
from abc import (ABCMeta, abstractmethod)
from static_site.settings import get_settings
from static_site.utils import get_rewriter


def rewrite(p):
    for v in get_settings('REWRITERS'):
        p = get_rewriter(v).rewrite(p)
    return p


class Rewriter(object):
    '''
    Abstract class for Rewriter.

    Rewriter must have 
        __init__(self) method 
    and
        rewrite(path) method                   
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def rewrite(path):
        raise NotImplementedError()


class RegexRewriter(Rewriter):
    '''
    Rewrite the path by the regex rules.

    >>> r = RegexRewriter((
    ...         (r'/$', r'/index'),
    ...     ))
    >>> r.rewrite('/')
    '/index'
    >>> r.rewrite('/music/')
    '/music/index'
    '''

    def __init__(self, rules=None):
        if rules:
            self.rules = rules
        else:
            self.__init__(get_settings('REGEX_REWRITER_RULES'))

    def rewrite(self, p):
        for old, new in self.rules:
            p = re.sub(old, new, p)
        return p


class ExtensionRewriter(Rewriter):
    '''
    Add the extension if the path doesn't have any extensions.

    >>> r = ExtensionRewriter('html')
    >>> r.rewrite('index')
    'index.html'
    >>> r.rewrite('index.html')
    'index.html'
    >>> r.rewrite('index.')
    'index.'
    '''

    def __init__(self, ext=None):
        if ext:
            self.extension = ext
        else:
            self.__init__(get_settings('PAGE_EXTENSION'))

    def rewrite(self, p):
        sp = p.split('.')
    
        # p has a extension
        if len(sp) > 1:
            return p
        return '{0}.{1}'.format(p, self.extension)
