# Casos de uso - GameGuardian

**Actor:** Usuario (padre/tutor que busca juegos aptos para su hijo).

## Lista de casos de uso

Implementados:
- Buscar videojuego (desde TP1, con AVL desde TP4)
- Listar catálogo (TP1)
- Filtrar por clasificación ESRB (TP1)
- Explorar categorías (TP5)

Pendientes:
- Ver Top 10 por franja etaria (TP6)
- Recomendar juegos similares (TP7 a TP9)
- Votar clasificación

# 01-Buscar videojuego
- **Precondición:** el catálogo está cargado.
- **Flujo principal:** 1. El usuario elige "Buscar". 2. El sistema pide el título. 3. El usuario lo ingresa. 4. El sistema busca en el árbol AVL y muestra el juego con su clasificación.
- **Flujo alternativo:** si no existe, el sistema informa "No se encontró ese juego".

# 02-Listar catálogo
- **Precondición:** el catálogo está cargado.
- **Flujo principal:** 1. El usuario elige "Listar". 2. El sistema recorre el árbol en inorder y muestra todos los juegos ordenados alfabéticamente.

# 03-Filtrar por clasificación ESRB
- **Flujo principal:** 1. El usuario elige "Filtrar". 2. Ingresa la clasificación (E, E10+, T, M). 3. El sistema muestra los juegos con esa clasificación.
- **Flujo alternativo:** si ninguno coincide, no se muestra nada.

# 04-Ver Top 10 por franja etaria (pendiente)
- **Flujo principal:** el usuario elige una clasificación y el sistema muestra los 10 juegos mejor valorados de esa franja.

# 05-Recomendar juegos similares (pendiente)
- **Flujo principal:** el usuario ingresa un juego que le gustó y el sistema sugiere juegos similares aptos para la misma franja etaria.

# 06-Votar clasificación (pendiente)
- **Flujo principal:** el usuario se identifica con un nickname y vota si la clasificación ESRB le parece acertada, más alta o más baja.
- **Flujo alternativo:** si ya votó ese juego, el sistema lo informa y no registra el voto.