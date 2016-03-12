# -*- coding: utf-8 -*-
"""
    excchange.app
    ---------------
"""

import os
from smts.util import isWindows

from serving import WSGIServer

def getDefaultStaticDir():
    if isWindows():
        return os.path.expanduser("~")
    else:
        return os.environ["HOME"]

# default static directory is System user home directory
DEFAULT_STATIC_DIR = getDefaultStaticDir()


class Exchange(object):
    def __init__(self, static_dir=None):
        self.static_dir = static_dir if static_dir else DEFAULT_STATIC_DIR
    
    def run(self, host=None, port=None):
        if host is None:
            host = "127.0.0.1"
        if port is None:
            port = 8888

        print "Serveing on host: {0} \r\nport: {1} \r\n".format(host, port)
        
        def app():
            print "application starting ......"
        
        server = WSGIServer(host, port, app)
        server.serve_forever()
