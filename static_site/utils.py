def get_rewriter(name):
    from importlib import import_module
    sn = name.split('.')
    module = import_module('.'.join(sn[:-1]))
    instance = getattr(module, sn[-1])()
    return instance
