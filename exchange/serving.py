# -*- coding: utf-8 -*-
from exchange import handler as H
import socket

try:
	from SocketServer import BaseRequestHandler, TCPServer
except ImportError:
	from socketserver import BaseRequestHandler, TCPServer


class WSGIServer(TCPServer, object):
	# for test environment
	allow_reuse_allow = 1  

	def __init__(self, host, port, app, handler=None):
		if handler is None:
			handler = H.BaseRequestHandler
		TCPServer.__init__(self, (host, port), handler)
		self.appliation = app

	def server_bind(self):
		# defined in BaseHTTPServer.HTTPServer
		TCPServer.server_bind(self)
		host, port = self.socket.getsockname()[:2]
		self.server_name = socket.getfqdn(host)
		self.server_port = port

	def get_app(self):
		return self.appliation


def make_app(host=None, port=None):
	if host is None:
		host = "127.0.0.1"
	if port is None:
		port = 8888

	print "Serveing on host: {0} \r\nport: {1} \r\n".format(host, port)
	def app():
		print "app function ......"

	server = WSGIServer(host, port, app)
	server.serve_forever()

