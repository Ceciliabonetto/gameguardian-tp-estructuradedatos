# Requerimientos - GameGuardian

## Requerimientos funcionales

1 — El sistema debe permitir buscar un videojuego por título.
2 — El sistema debe permitir listar todos los videojuegos del catálogo.
3 — El sistema debe permitir filtrar videojuegos por clasificación ESRB (E, E10+, T, M, AO).
4 — El sistema debe permitir mostrar el Top 10 de videojuegos mejor valorados dentro de una franja etaria.
5 — El sistema debe permitir recomendar videojuegos similares a uno dado, dentro del mismo rango de edad permitido.
6 — El sistema debe permitir que un usuario vote si la clasificación ESRB de un juego le parece acertada, generando una clasificación complementaria basada en la comunidad.
7 — El sistema no debe permitir que un mismo usuario vote más de una vez por el mismo juego.

## Requerimientos no funcionales

1 — La búsqueda por título debe resolverse en tiempo logarítmico sobre el total de elementos (O(log n)). (implementado en TP3 mediante árbol binario de búsqueda). La búsqueda por título debe resolverse en tiempo logarítmico sobre el total de elementos (O(log n)). (TP3: árbol binario de búsqueda; TP4: AVL, que garantiza O(log n) sin importar el orden de inserción)
2 — El sistema debe soportar al menos 10.000 elementos sin degradar perceptiblemente el tiempo de respuesta.
3 — La interfaz debe ser accesible por línea de comandos, sin requerir conocimientos técnicos del usuario final.
4 — Los datos del catálogo deben poder cargarse desde un archivo JSON externo, sin necesidad de modificar el código fuente.

## Alcance y fuera de alcance

**Dentro del alcance:**
- Catálogo de videojuegos con clasificación ESRB y clasificación comunitaria.
- Búsqueda, listado, filtrado y ranking de videojuegos.
- Sistema de recomendación por similitud entre juegos.
- Sistema de votos comunitarios sobre la clasificación ESRB.

**Fuera de alcance:**
- No se implementa autenticación de usuarios (el nombre de usuario se usa solo para identificar votos, sin contraseña ni sesión).
- No se implementa una interfaz gráfica ni web (solo terminal).
- No se conecta con APIs externas de videojuegos en tiempo real (los datos son estáticos, cargados desde JSON).

## Historial de avance

- **TP0**: definición de idea, dominio, problema, usuario objetivo (ver propuesta enviada al docente).
- **TP1**: clase `Videojuego`, carga desde JSON, interfaz de terminal con buscar/listar/filtrar.
- **TP2**: comparación de búsqueda secuencial (O(n)) vs binaria (O(log n)), medición con 100/1.000/10.000 elementos.
- **TP3**: árbol binario de búsqueda (`ArbolBST`) ordenado por título, con inserción, búsqueda y recorridos inorder/preorder/postorder. Integrado a las opciones "Buscar" y "Listar" del menú, reemplazando la lista simple.
- **TP4**: árbol AVL (`ArbolAVL`) con las cuatro rotaciones, integrado al menú en lugar del BST. Experimento con datos ordenados: el BST degenera (altura = N) y el AVL mantiene altura ≈ log₂ N (ver `docs/06-analisis-avl.md`).