import importlib.metadata

class Version(object):
    def __str__(self):
        return importlib.metadata.version('insPyred-print')
