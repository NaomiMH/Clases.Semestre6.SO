#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import time
# para crear arreglos
import numpy as np
# para mostrar tablas
from tabulate import tabulate
# para el redondeo
from math import floor
from math import ceil

# Inicializacion

# Variables en valores negativos
# El programa no correra si los valores no son cambiados a valores aceptables
RealMemory = -1
SwapMemory = -1
PageSize = -1
PoliticaMemory = 'XXX'
# Memoria total disponible
# unidades en marcos
M_DIS = 0

# Variables limites
# Estos limites pueden ser cambiados
RM_MAX = 10
RM_MIN = 0
SM_MAX = 10
SM_MIN = 0
PS_MAX = 10000
PS_MIN = 0

# Variable Arreglo de Procesos
# [Timestamp entrada, Timestamp salida, # de Marcos totales, # de Tamano del proceso]
Proc=np.full((10,4),-1)

# Manejo de errores
mError = np.array(['* Error: Valor fuera de limite > RealMemory','* Error: Valor fuera de limite > SwapMemory','* Error: Valor fuera de limite > PageSize','* Error: Inicializacion incompleta','* Error: commando desconocido',' * Error: Politica incompleta','* Error: Proceso invalido > ','* Error: Memoria requerida','* Error: Proceso invalido >','* Error: Direccion virtual invalida >','* Error: Accion invalida >','* Error: Proceso invalido > ','* Error: Algoritmno invalido > PoliticaMemory'])

# Funciones

# Arreglo de errores
# Parametro: Numero identificador de error
def manejodeErrores(error):
	if(mError[error] > 6 and error != 13):
		Errorcompleto = mErrror[error] + data
	if(mError[error] == 13):
		Errorcompleto = mErrror[error]
	salir()

# Inicializar la memoria Swap y Real
# Parametro: Tamano de la memoria real y Tamano de la memoria swap
def iniciarMemoria():
	# Variable Arreglo de RealMemory y SwapMemory
	# [# identificador, Timestamp entrada a RM, Contador usos]
	print "Memoria inicializada"
	RM = np.full((int(ceil(RealMemory*1024/PageSize)),3),-1)
	SM = np.full((int(ceil(SwapMemory*1024/PageSize)),3),-1)

# Desconexion y salida
def salir():
	print >>sys.stderr, 'Salida'
	connection.close()
	sys.exit()

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
	print >>sys.stderr, 'Function liberar'
	print Proc
	Proc[proceso,0]*=-1
	print Proc

# Buscar Direccion disponible para remplazar
# Return: Direccion de la memoria real
def buscar():
	if (PoliticaMemory is 'LRU'):
		return aLRU();
	elif (PoliticaMemory is 'MFU'):
		return aMFU();

# Acceso
# Parametro: Numero de proceso a accesar, direccion virtual, accion (escritura = 1, lectura = 0)
def acceso(proceso,dirvir,accion):
	print >>sys.stderr, 'Function acceso INCOMPLETA'

# Proceso
# Parametro: Numero del proceso, Tamano del proceso, Numero de marcos.
def proceso(proceso,tamano,marcos):
	print >>sys.stderr, 'Function proceso INCOMPLETA'
	# agregando proceso a la matriz de Proceso
	# Timestamp entrada
	Proc[proceso,0]=0.1
	# Timestamp salida (que aun no es inicializada)
	# # de Marcos totales
	Proc[proceso,2]=marcos
	# # de Tamano del proceso
	Proc[proceso,3]=tamano

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
				break
			elif ('RealMemory' in data):
				# Guardando variables
				RealMemory = int(data[11:])
				M_DIS += RealMemory*1024
				# Comprobando variables
				# RM_MIN < RealMemory < RM_MAX
				if (RM_MIN > RealMemory or RM_MAX < RealMemory):
					manejodeErrores(1)
			elif ('SwapMemory' in data):
				# Guardando variables
				SwapMemory = int(data[11:])
				M_DIS += SwapMemory*1024
				# Comprobando variables
				# SM_MIN < SwapMemory < SM_MAX
				if (SM_MIN > SwapMemory or SM_MAX < SwapMemory):
					manejodeErrores(2)
			elif ('PageSize' in data):
				# Guardando variables
				PageSize = int(data[9:])
				M_DIS = ceil(M_DIS/PageSize)
				# Comprobando variables
				# PS_MIN < PageSize < PS_MAX
				if (PS_MIN > PageSize or PS_MAX < PageSize):
					manejodeErrores(3)
				# iniciar la memoria real y swap con tamano en marcos
				iniciarMemoria(ceil(RealMemory*1024/PageSize),ceil(SwapMemory*1024/PageSize))
			elif ('PoliticaMemory' in data):
				# Las variables deben de ya haber sido inicializadas
				if (RealMemory == -1 or SwapMemory == -1 or PageSize == -1):
					manejodeErrores(4)
				# Guardando variables
				PoliticaMemory = data[15:]
				# Comprobando variables
				# PoliticaMemory = LRU o MFU
				if ('LRU' != PoliticaMemory and 'MFU' != PoliticaMemory):
					manejodeErrores(13)
			elif (data[0] == 'P'):
				# PoliticaMemory ya debio de haber sido especificado
				if (PoliticaMemory == 'XXX'):
					manejodeErrores(6)
				# Crear proceso #Pnum con tamano #Pbyte
				# Buscando espacios
				esp = data.find(' ')
				esp2 = data.find(' ',esp+1)
				# Guardando variables
				Pbyte = int(data[esp:esp2])
				Pmar = ceil(Pbyte/PageSize)
				Pnum = int(data[esp2:])
				# Comprobando variables
				# Proc en la posicion Pnum debe de tener un numero invalido (menor a 0)
				# Pbyte debe de ser menor o igual al espacio disponible
				if (Proc[Pnum][0] > 0 or Pnum < 0):
					manejodeErrores(7)
				elif (Pmar > M_DIS or Pmar < 0):
					manejodeErrores(8)
				else:
					# Mandando Pbyte, Pmar y Pnum a la funcion proceso
					proceso(Pnum,Pbyte,Pmar)
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
				# Comprobando variables
				# Proc en la posicion Anum debe de tener un numero valido (mayor a 0)
				# Adv debe de ser menor al tamano del proceso
				# Acc tiene que ser 0 o 1
				if (Proc[Anum][0] < 0 or Anum < 0):
					manejodeErrores(9)
				elif (Adv > Proc[Anum][3] or Adv < 0):
					manejodeErrores(10)
				elif (Acc > 1 or Acc < 0):
					manejodeErrores(11)
				else:
					# Mandando Adv, Anum, Acc a la funcion acceso
					acceso(Anum,Adv,Acc)
			elif (data[0] == 'L'):
				# Liberar el proceso #Lnum
				# Guardando variables
				Lnum = int(data[1:])
				# Comprobando variables
				# Proc en la posicion Lnum debe de tener un numero valido (mayor a 0)
				if (Proc[Lnum][0] < 0 or Lnum < 0):
					manejodeErrores(12)
				# Manda Lnum a la funcion liberar
				liberar(Lnum)
			elif (data[0] == 'C'):
				# Desplegar comentario
				print >> sys.stderr, data[2:]
			else:
				# Si no es ninguno commando de los anteriores, es error.
				manejodeErrores(5)
		else:
			print >>sys.stderr, 'No data from', client_address
			salir()
finally:
	# Clean up the connection
	salir()

#When communication with a client is finished, the connection needs to be cleaned up using close(). This example uses a try:finally block to ensure that close() is always called, even in the event of an error.

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
