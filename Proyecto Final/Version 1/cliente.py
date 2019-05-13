#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The client program sets up its socket differently from the way a server does. Instead of binding to a port and listening, it uses connect() to attach the socket directly to the remote address.

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.

messages = ['C comenzamos...', 'RealMemory 2', 'SwapMemory 4', 'PageSize 16', 'P 2048 1', 'A 3 2 1', 'L 1', 'F']
try:
    # Send data
    for m in messages:
		print >>sys.stderr, '%s' % m
		sock.sendall(m)

		# Look for the response

		respuesta = sock.recv(256)
		print >>sys.stderr, '>>%s' % respuesta

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

def main(args):
    return 0
