# AP-automodelcar
Proyecto de Ampliación de Robótica
Objetivo: recorrer pista que simula entorno urbano:
* Challenge 1: reconocer pista y recorrerla de forma autónoma:
  ENodo de seguir linea --> Mario y Felipe
 * Challenge 2: igual, pero con obstáculos fijos y móviles:
  No tengo mucha idea pero creo que debemos utilizar costmap_2d:
  http://wiki.ros.org/costmap_2d
* Challenge 3: igual, pero con semáforos y aparcamientos:
  En este caso, crearemos un nodo que publique un topic o un servicio(en modo servicio no está hecho) que indique si ha visto una señal de stop. 

Tareas
* Crear mundo linea --> Juanlu
* Crear robot+sensores --> Alfonso
* Crear señal de stop --> Fran
* Crear nodo seguidor de linea --> Felipe y Mario
* Crear listener para escuchar los datos de seguidor de linea y reconocimiento visual
