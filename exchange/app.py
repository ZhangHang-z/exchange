import os
from smts.util import isWindows


def getDefaultStaticDir():
    if isWindows():
        return os.path.expanduser("~")
    else:
        return os.environ["HOME"]

# default static directory is System user home directory
DEFAULT_STATIC_DIR = getDefaultStaticDir()


class Exchange(object):
    def __init__(self, static_dir=None):
        self.static_dir = static_dir if static_dir else self.DEFAULT_STATIC_DIR
        
        
        