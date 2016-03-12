# -*- coding: utf-8 -*-
"""
    maybeHot.serve
    ---------------
 
    There has a straightly way to extends Core Library Class,
    which is BaseHTTPServer.BaseHTTPRequestHanler.
    But I think it's even so lowly.
"""

import socket
import time
import sys
import smts
import urlparse

from warnings import filterwarnings, catch_warnings
import path
with catch_warnings():
    if sys.py3kwarning:
        filterwarnings("ignore", "*mimetools has been removed",
                    DeprecationWarning)
        import mimetools

try:
    # for py2.
    import SocketServer
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    # for py3, it was renamed.
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import socketserver as SocketServer


DEFAULT_ERROR_MESSAGE = """
<html>
<title>Error Occured</title>
<body>
<h1>Error</h1>
<p>Error Code: {0}</p>
<p>Message: {1}</p>
</body>
</html>
"""


class BaseRequestHandler(BaseHTTPRequestHandler, object):
    _VERSION = "exchange/0.1"

    # defult http procotol version.
    DEFAULT_HTTP_VERSION = "HTTP/1.1"
    
    DEFAULT_HTTP_SCHEME = "http"

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if not self.raw_requestline:
                self.close_connection = True
            elif self.parse_request():
                return self.run_wsgi()
        except socket.timeout as e:
            self.log_error("Request Time Out {0}".format(e))
            self.close_connection = True
            return

    def run_wsgi(self):
        print self.request.recv(1024)
        print self.path
        print self.raw_requestline
        print "--------------"
        self.set_environ()
        self.send_response()
        self.send_headers("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        # run application
        app = self.server.get_app()
        app()

        self.send_body()
        self.finish()

    def set_environ(self):
        """parse A URL.
        e.g. <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        """
        scheme, netloc, path, params, query, fragment = \
            urlparse.urlparse("http://example.com%s" % self.path)
        scheme = scheme or self.DEFAULT_HTTP_SCHEME or "http"
        
        self.env = {
            "wsgi.url_scheme":      scheme,
            "wsgi.input":           self.rfile,
            "wsgi.errors":          sys.stderr,
            "REQUEST_METHOD":       self.command,
            "PATH_INFO":            self.path,
            "QUERY_STRING":         query,  
            "CONTENT_TYPE":         self.headers.get("Content-Type", ""),
            "CONTENT_LENGTH":       self.headers.get("Content-Length", ""),
            "CLIENT_ADDR":          self.client_address[0],
            "CLIENT_PORT":          self.client_address[1],
            "SERVER_ADDR":          self.server.server_address[0],
            "SERVER_PORT":          self.server.server_address[1]
        }

    def handle(self):
        rv = super(BaseRequestHandler, self).handle()
        return rv

    def send_body(self, html_source_codes=None):
        with open("C:\\index.html") as f:
            html = f.read()
        html_source_codes = html
        if html_source_codes is None:
            html_source_codes = "<code>No provided html</code>"
        self.request.sendall(html_source_codes)

    def format_req_head(self):
        request_head = self.request.recv(1024).strip()
        return request_head.rstrip('\n')

    def send_response(self):
        self.wfile.write("{0} {1} {2}\r\n".format("HTTP/1.1", 200, "OK"))
        self.wfile.write("{0}: {1}\r\n".format("Date", self.date_header()))

    def send_headers(self, k, v):
        self.wfile.write("{0}: {1}\r\n".format(k, v))

    def end_headers(self):
        # see HTTP Protocol RFC2616, ended with a space line.
        self.wfile.write("\r\n")

    def date_header(self, timestamp=None):
        if not timestamp:
            timestamp = time.time()
        date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(timestamp))
        return date

