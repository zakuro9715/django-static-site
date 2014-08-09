REWRITERS = (
    'static_site.rewriter.RegexRewriter',
    'static_site.rewriter.ExtensionRewriter',
)

REGEX_REWRITER_RULES = (
    ('/$', '/index'),
)

PAGE_EXTENSION = 'html'
