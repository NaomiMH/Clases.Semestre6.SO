#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts by creating a TCP/IP socket.

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.
# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().
try:
	print >>sys.stderr, 'connection from', client_address

	# Receive the data 
	while True:   
		data = connection.recv(256)
		print >>sys.stderr, 'Analizando: "%s"' % data
		if data:
			print >>sys.stderr, 'sending answer back to the client'

			# identificacion de comandos
			if (data[0]=='F'):
				print >>sys.stderr, 'Fin'
				connection.sendall(' ' + data)	
			elif (data[1]=='e'):
				RealMemory = int(data[11:])
				print >>sys.stderr, 'init RealMemory = %d' % RealMemory
				connection.sendall(' RealMemory is ' + data[11:])
			elif (data[1]=='w'):
				SwapMemory = int(data[11:])
				print >>sys.stderr, 'init SwapMemory = %d' % SwapMemory
				connection.sendall(' SwapMemory is ' + data[11:])
			elif (data[1]=='a'):
				PageSize = int(data[9:])
				print >>sys.stderr, 'init PageSize = %d' % PageSize
				connection.sendall(' PageSize is ' + data[9:])
			# si es una C, un comentario, solo enviar de regreso
			elif (data[0]=='C'):
				print >>sys.stderr, 'Comentario'
				connection.sendall(' ' + data)
			elif (data[0]=='P'):
				esp = data.find(' ')
				esp2 = data.find(' ',esp+1)
				Pbyte = int(data[esp:esp2])
				Pnum = int(data[esp2:])
				print >>sys.stderr, 'Cargar al proceso num %d' % Pnum
				print >>sys.stderr, 'Asignando %d bytes' % Pbyte
				connection.sendall(' ' + data)
			elif (data[0]=='A'):
				esp = data.find(' ')
				esp2 = data.find(' ',esp+1)
				esp3 = data.find(' ',esp2+1)
				Adv = int(data[esp:esp2])
				Anum = int(data[esp2:esp3])
				Acc = int(data[esp3:])
				print >>sys.stderr, 'Acceder al proceso num %d' % Anum
				print >>sys.stderr, 'Direccion virtual %d' % Adv
				print >>sys.stderr, 'Accion %d' % Acc
				connection.sendall(' ' + data)
			elif (data[0]=='L'):
				Lnum = int(data[1:])
				print >>sys.stderr, 'Liberar al proceso num %d' % Lnum
				connection.sendall(' ' + data)
			else:
				print >>sys.stderr, 'error 2'
		else:
			print >>sys.stderr, 'no data from', client_address
			connection.close()
			sys.exit()

finally:
	# Clean up the connection
	print >>sys.stderr, 'se fue al finally'
	connection.close()

#When communication with a client is finished, the connection needs to be cleaned up using close(). This example uses a try:finally block to ensure that close() is always called, even in the event of an error.

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
