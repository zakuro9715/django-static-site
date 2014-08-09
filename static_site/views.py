from django.shortcuts import render
from django.http import HttpRequest, Http404
from django.template import TemplateDoesNotExist

from static_site import rewriter
# Create your views here.

def page(request, path):
    
    # if top of path is not '/', insert '/' into a top of path.
    p = path
    if not len(p) or p[0] != '/':
        p = '/' + p

    p = rewriter.rewrite(p)
    try:
        # p[0] is '/' 
        return render(request, p[1:])
    except TemplateDoesNotExist:
        raise Http404('The requested URL /{0} was not found'.format(path))
