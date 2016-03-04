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

from utils import Codes

try:
	# for py2.
	import SocketServer
except ImportError:
	# for py3, it's renamed.
	import socketserver as SocketServer


class BaseRequestHandler(SocketServer.StreamRequestHandler, object):
	_VERSION = "maybeHot/0.1"

	# defult http procotol version.
	DEFAULT_HTTP_VERSION = "HTTP/1.1"

	def handle(self):
		request_head = self.request.recv(1024).strip()
		# print request_head.split('\n');
		# print "{} wrote:".format(self.client_address)
		self.send_response()
		self.send_headers("Content-Type", "text/html; charset=utf-8")
		self.end_headers()
		# Response body
		app = self.server.get_app()
		app()
		self.send_body()
		self.finish()

	def send_body(self, html_source_codes=None):
		if html_source_codes is None:
			html_source_codes = "<code>No provided html</code>"
		self.request.sendall(html_source_codes)

	def format_req_head(self):
		request_head = self.request.recv(1024).strip()
		return request_head.rstrip('\n');

	def send_response(self):
		self.wfile.write("{0} {1} {2}\r\n".format("HTTP/1.1", 200, "OK"))
		self.wfile.write("{0}: {1}\r\n".format("Date", self.date_header()))
		
	def send_headers(self, k, v):
		self.wfile.write("{0}: {1}\r\n".format(k, v))

	def end_headers(self):
		# see RFC 2616.
		self.wfile.write("\r\n")


	def date_header(self, timestamp=None):
		if not timestamp:
			timestamp = time.time()
		date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(timestamp))
		return date


if __name__ == "__main__":
	HOST, PORT = "localhost", 8888
	server = SocketServer.TCPServer((HOST, PORT), BaseRequestHandler)
	server.serve_forever()