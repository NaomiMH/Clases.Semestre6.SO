#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts by creating a TCP/IP socket.

import socket
import sys
import time
from tabulate import tabulate

# Inicializacion

# Variables en valores negativos
# El programa no correra si los valores no son cambiados a valores aceptables
RealMemory = -1
SwapMemory = -1
PageSize = -1
PoliticaMemory = 'XXX'

# Funciones

# Algoritmos de reemplazo
# Return: Marco de pagina de la memoria real
def aLRU():
	print >>sys.stderr, 'Function LRU INCOMPLETA'
	return 0;

def aMFU():
	print >>sys.stderr, 'Funtcion MFU INCOMPLETA'
	return 0;

# Liberacion del proceso
# Parametro: Numero de proceso a liberar
def liberar(proceso):
	print >>sys.stderr, 'Function liberar INCOMPLETA'

# Buscar Direccion disponible para remplazar
# Parametro: Iniciales del algoritmo de reemplazo a utilizar
# Return: Direccion de la memoria real
def buscar(algoritmo):
	print >>sys.stderr, 'Function buscar INCOMPLETA'

# Acceso
# Parametro: Numero de proceso a accesar, direccion virtual, accion (escritura = 1, lectura = 0)
def acceso(proceso,dirvir,accion):
	print >>sys.stderr, 'Function acceso INCOMPLETA'

# Proceso
# Parametro: Numero del proceso, tamano.
def proceso(proceso,tamano):
	print >>sys.stderr, 'Function proceso INCOMPLETA'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'Starting up on %s port %s' % server_address
sock.bind(server_address)

# Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.
# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'Waiting for a connection'
connection, client_address = sock.accept()

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().
try:
	print >>sys.stderr, 'Connection from', client_address

	# Receive the data 
	while True:   
		data = connection.recv(256)
		connection.sendall(' ' + data)
		print >>sys.stderr, 'Input: "%s"' % data
		if data:
			# Identificacion de comandos
			if (data == 'F'):
				print >>sys.stderr, 'End of the program'
				connection.close()
				sys.exit()
			elif ('RealMemory' in data):
				# Guardando variables
				RealMemory = int(data[11:])
			elif ('SwapMemory' in data):
				# Guardando variables
				SwapMemory = int(data[11:])
			elif ('PageSize' in data):
				# Guardando variables
				PageSize = int(data[9:])
			elif ('PoliticaMemory' in data):
				# Guardando variables
				PoliticaMemory = data[15:]
				print >>sys.stderr, '"%s"' % PoliticaMemory
			elif (data[0] == 'P'):
				# Crear proceso #Pnum con tamano #Pbyte 
				# Buscando espacios
				esp = data.find(' ')
				esp2 = data.find(' ',esp+1)
				# Guardando variables
				Pbyte = int(data[esp:esp2])
				Pnum = int(data[esp2:])
				# Mandando Pbyte y Pnum a la funcion proceso
				proceso(Pnum,Pbyte)
			elif (data[0] == 'A'):
				# Acceder a proceso #Anum con direccion virtual #Adv para #Acc (leer/escribir)
				# Buscando espacios				
				esp = data.find(' ')
				esp2 = data.find(' ',esp+1)
				esp3 = data.find(' ',esp2+1)
				# Guardando variables
				Adv = int(data[esp:esp2])
				Anum = int(data[esp2:esp3])
				Acc = int(data[esp3:])
				# Mandando Adv, Anum, Acc a la funcion acceso
				acceso(Anum,Adv,Acc)
			elif (data[0]=='L'):
				# Liberar el proceso #Lnum
				# Guardando variables
				Lnum = int(data[1:])
				# Manda Lnum a la funcion liberar
				liberar(Lnum)
			elif (data[0] != 'C'):
				# Ignora comentarios
				# Si no es ninguno de los anteriores, ni un comentario, es error.
				print >>sys.stderr, 'error 2'
				connection.close()
				sys.exit()
		else:
			print >>sys.stderr, 'No data from', client_address
			connection.close()
			sys.exit()

finally:
	# Clean up the connection
	connection.close()

#When communication with a client is finished, the connection needs to be cleaned up using close(). This example uses a try:finally block to ensure that close() is always called, even in the event of an error.

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
