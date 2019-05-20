# Proyecto Final
Miembros

Naomi Macias Honti A01282098

Mario Roque Chairez A01282301

## Version 1
Ejecucion del programa base

Se investigo sobre los comandos necesarios para correr el programa.
Se inicializaron las variables que se esperan recibir por el cliente.
Cada comando que se reciba del cliente regresa una confirmacion de entregado (mismo mensaje recibido con un espacio agregado
como comprobacion).
El servidor muestra las variables recibidas como comprobacion de extracion exitosa (las variables son enviados junto con el
comando en una string y se guardan en una variable int).

Meta:

Los comandos son reconocidos, todas las variables estan funcionando, el programa no cierra abrutamente a causa de errores
de usuario y los valores ingresados son los correspondientes a cada variable. Se asigna el espacio correspondiente a cada
funcion que sera requerida con el objetivo de mantener el codigo ordenado. Cada posible error es reconocido y anunciado
al usuario.

## Version 1.1
Correccion y limpieza

Se agrega una inicializacion de valores invalidos para las variables.
Reorganizacion de la lectura de comandos.
Se quitan las evidencias de las variables recibidas.
Tras reconocer el commando y obtener los valores recibidos, se llama a la funcion correspondiente (para todos los comandos,
excepto para aquellos que solo inicializan una variable).
Se agregan las funciones vacias necesarias.

Problema a resolver:

Se encuentra dificultades para cerrar correctamente la conexion. Aun cuando no sale ningun error y se ejecuta bien el
programa, la conexion tarda en liberarse.

Falta:

Comprobar que los valores de las variables sean correctas y que se inicialicen las variables necesarias antes de que lleguen
los otros comandos.

## Version 1.2
Comprobacion de variables

Implementacion de las funciones floor y ceil para resolver los redondeos.
Funcion especifica para salir, se cambian las llamadas de salida por la llamada a la funcion de salida.
Se establecen variables para controlar los limites para los posibles valores de las variables recibidas.
Reconocimiento de errores, aviso de tipo de error y sale del programa.
Las variables son inicializadas con valores invalidos, por lo que si no se inicializan, daran error.
Se comprueban dependencias de variables, antes de inicializar la estrategia de reemplazo, se debio de inicializar la memoria real, swap y pagesize, antes de crear cualquier proceso, se debio inicializar la estrategia.
Se creo una variable del tamano equivalente de la memoria real mas la memoria swap en marcos, se utiliza para llevar control de la cantidad de marcos totales disponibles.
Se crea una matriz de procesos donde el proceso n se guarda en la posicion n, contienendo su tiempo de llegada, salida, su tamano en byte y sus marcos.
Implementacion de Numpy para crear la matrices.

Problema a resolver:
Cuando sale del servidor por un error de las variables recibidas, el cliente no se cierra correctamente.
A la hora de recibir el commando F, para terminar el programa, se tiene que verificar que todos los procesos hayan sido liberados correctamente.

## Version 2
Creacion de memoria

Se inicializa la memoria real y la memoria swap segun su tamano correspondiente en marcos


# Version 2.1

Comentarios
utilizando funcion inicializacion

# Version 2.2

Corregido la funcion inicializacion

# Version 3

Errores

# Version 3.1

Funciones proceso, acceso, estrategias de reemplazo y liberacion. Se agrega historial.

# Version 3.2

Lo que hizo mario
