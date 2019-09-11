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

## Version 2 - 3.2
Creacion de memoria

Creacion de funcion de inicializacion

Corrigiendo funcion de inicializacion

Corrigiendo Errores

Creacion de funciones: proceso, acceso, estrategias de reemplazo y liberacion. Creacion de tabla de historial.

Creacion de la tabla de fallas.

Se inicializa la memoria real y la memoria swap segun su tamano correspondiente en marcos.
Se crea y corrige una funcion para inicializar la memoria real y swap con los tamanos que sean indicados entre los comandos de entrada.
Se corrigen errores de procesamiento.
Se crean funciones como:
Proceso, donde un proceso llega a la memoria y es asignado en algun lugar libre en la memoria.
Acceso, llega una peticion de acceder a un proceso n con un desplazamiento x. Dicho desplazamiento es correspondiente a uno de los marcos del proceso, dicho marco puede encontrarse en la memoria real o swap, en el caso de encontrarse en la memoria swap, este marco sera movido a la momria real, de no encontrar espacio, con la estrategia de reemplazo, se le asigna un lugar.
Estrategia de reemplazo, definido entre los comandos de entrada, regresa un marco en la memoria real que puede estar libre o ocupado por otro marco. Dicho marco es elegido por la estrategia de reemplazo.
Liberacion, un proceso n es borrado de la memoria real y swap.
Creacion de la tabla de historial, contiene informacion sobre el comando que llega y el resultado en la memoria swap y real, asi como un listado de los procesos que fueron liberados.
Creacion de la tabla de fallas, contiene un contador de la cantidad de fallas en memoria. Cuando un marco de un proceso no se encuentra en memoria real.

Nota: se perdieron los detalles de cada cambio de version al acercarse la fecha de entrega, a causa de que los cambios comenzaron a ser mas pequenos y en fechas muy cercanas.

## Entrega del proyecto
Retroalimentacion

Cuando un proceso llega primero es guardado en la memoria real, sin importar si esta esta llena, si no tiene espacio se liberan los marcos necesarios atraves de la estrategia de reemplazo correspondiente.
En la tabla de fallas, solo se tiene que contar cuando llega una peticion de acceso y el marco del proceso al que se quiere acceder no se encuentra en la memoria real.
