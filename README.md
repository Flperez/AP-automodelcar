# AP-automodelcar
Proyecto de Ampliación de Robótica
Objetivo: recorrer pista que simula entorno urbano:
* Challenge 1: reconocer pista y recorrerla de forma autónoma
  ** Ejecutar el line_detection_fu  --> Este paquete reconoce las líneas de una carretera
* Challenge 2: igual, pero con obstáculos fijos y móviles
  ** No tengo mucha idea pero creo que debemos utilizar costmap_2d:
  http://wiki.ros.org/costmap_2d
* Challenge 3: igual, pero con semáforos y aparcamientos:
  ** En este caso, crearemos un nodo que publique un topic o un servicio(en modo servicio no está hecho) que indique si ha visto una señal de stop. 

Objetivo del trabajo:
*  Poner en marcha el robot
*  Implementar y probar funciones de control del coche
*  Implementar y probar funciones de reconocimiento del entorno (Deteccin de semáforos, señales de tráfico, peatones...)
*  Implementar y probar funciones de estimación de posición y  localización
