# Monitores
25 Marzo 2019

2 horas

## Instrucciones
Se pide implantar una solución concurrente al ejercicio del Transbordador.

Simule las funciones ir y volver, mediante un mensaje de texto: La función ir mandaría el mensaje “Parte de ida el transbordador”
y la función volver enviaría el mensaje “Parte de regreso el transbordador”.

Se solicita ejecutar al menos 100 iteraciones.

## Ejercicio Transbordador
Un transbordador permite pasar coches de un lado de un rio al otro.

Los coches viajan por el lado este del rio, cruzan el rio y despues viajan por el lado oeste (nunca vuelven). El transbordador tiene una 
capacidad de 10 coches y espera a estar lleno para cruzar el rio. Cuando ha cruzado y descargado los coches vuelve vacio.

Se pide implantar este problema resolviendo la concurrencia con el empleo de un monitor. En el caso en que quiera desbloquear a varios
 procesos (Signal), esto debeb de hacerse en cascada, es decir; el que sale debe desbloquear al siguiente y este al siguiente y asi
 sucesivamente.
