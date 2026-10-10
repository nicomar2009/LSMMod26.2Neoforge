# Pendientes invertidas sin baranda

Diez bloques nuevos e independientes: `school_inverted_slope_split_1..4` y `school_inverted_slope_flight_1..6`. Conservan las pendientes de sus respectivas piezas con baranda (5/7 y 2/3), pero contienen únicamente pared clara. Sus nombres traducidos aparecen en la pestaña creativa. Un ítem coloca una pieza; romperla devuelve solo ese ítem.

Se invierte la geometría en Y después de retirar el desplazamiento inicial de 12 píxeles: **Y nueva = 12/16 − Y original**. El primer borde inclinado empieza en Y=0; la cara plana queda arriba, en Y=16 píxeles de cada celda. Los cantos inclinados descienden en la dirección horizontal del jugador. Para ver la subida en sentido contrario, gira las piezas. No existe un estado HALF: son variantes invertidas fijas, separadas de los originales.

## Montaje desde el extremo superior

Las alturas se expresan respecto de la celda de la primera pieza; valores negativos significan colocar más abajo.

| Tramo | Pieza | Avance | Altura de celda |
| --- | --- | --- | --- |
| Interrumpido | 1 | 0 | 0 |
| Interrumpido | 2 | 1 | -1 |
| Soporte oscuro | — | 2–4 | según el edificio |
| Interrumpido | 3 | 5 | -4 |
| Interrumpido | 4 | 6 | -5 |
| Continuo | 1 | 0 | 0 |
| Continuo | 2 | 1 | -1 |
| Continuo | 3 | 2 | -2 |
| Continuo | 4 | 3 | -2 |
| Continuo | 5 | 4 | -3 |
| Continuo | 6 | 5 | -4 |

Todas las piezas del montaje miran hacia el descenso. El tramo interrumpido conserva las columnas ocultas por el soporte de tres bloques, sin geometría dentro de ellas. El continuo conserva los seis bloques de recorrido y cuatro de desnivel del montaje superior, pero su borde inicial parte de cero en lugar de 12 px.

Se añaden los cuatro píxeles superiores que faltaban: únicamente la tapa plana pasa de Y=12 a Y=16 px. El borde inclinado, las UV, las posiciones y el inicio Y=0 se conservan. La colisión cubre también esa extensión.

Los modelos OBJ tienen caras planas y normales corregidas tras la reflexión. UV originales de pared clara, sin materiales metálicos. Cuatro orientaciones, espejo, rotación y agua. Selección con caja simple, colisión precalculada independiente con una aproximación de medio píxel como máximo. La parte inclinada puede salir por debajo de la celda; deja ese volumen libre al montarla. No se colocan celdas auxiliares ni relleno automáticamente.

Generador: `tools/create_school_inverted_slopes.py`; comprobación estática: `tools/check_school_inverted_slopes.py`; montaje: `tools/school_inverted_slope_layout.json`; vista previa externa: `previews/school_inverted_slopes.png`.

80 estados nuevos verificados mediante análisis estático: reflexión exacta del muro original, inicio Y=0, ausencia de baranda, continuidad, UV, volúmenes y caras exteriores. Sin compilación ni ejecución de Minecraft.

## Copias elevadas ocho píxeles

Los bordes inclinados de `school_inverted_slope_flight_raised_1..6` y `school_inverted_slope_split_raised_1..4` están exactamente +8 píxeles en Y respecto a las piezas originales. Se conservan la pendiente, el ancho, la profundidad, las caras, UV y texturas, sin baranda. Únicamente las tapas planas se ajustan al límite entero del bloque superior:

| Familia | Piezas | Tapa local Y | Cambio desde la copia de 24 px |
| --- | --- | --- | --- |
| flight | 1, 4, 5 | 16 px | −8 px |
| flight | 2, 3, 6 | 32 px | +8 px |
| split | 1, 3 | 16 px | −8 px |
| split | 2, 4 | 32 px | +8 px |

En split se aplica el remate por parejas a ambos lados del soporte de tres columnas. La colisión utiliza la misma altura superior que cada modelo, conservando el contorno de selección simple separado de la colisión.

Usa la tabla de colocación de las piezas originales: filas 0, -1, -2, -2, -3, -4 para flight; filas 0, -1, -4, -5 en columnas 0, 1, 5, 6 para split. No cambies la altura de colocación para conseguir el desplazamiento: ya está en los modelos. Deja libres las celdas ocupadas por las extensiones hacia arriba. Los ítems y drops son independientes de los originales.

Generador: `tools/create_school_raised_inverted_slopes.py`; verificación: `tools/check_school_raised_inverted_slopes.py`; layout: `tools/school_raised_inverted_slope_layout.json`. Se verifican los 80 estados elevados: tapas, traslación del perfil en las cuatro orientaciones, UV/caras/materiales y colisión. Regresión de las piezas originales y con baranda. Sin compilación ni prueba Minecraft.

## Piezas extra de la zona del soporte

Solo se añaden `school_inverted_slope_split_raised_extra_1..3`; no hay extras sin elevar, con baranda ni de flight. Completan las columnas antes omitidas y mantienen el perfil continuo de 7 columnas y 5 bloques de desnivel, elevado 8 px. Misma orientación hacia el descenso y textura de pared clara.

| Extra | Columna | Fila relativa | Tapa local |
| --- | --- | --- | --- |
| 1 | 2 | -2 | 32 px |
| 2 | 3 | -3 | 32 px |
| 3 | 4 | -3 | 16 px |

Las tapas alcanzan el siguiente límite entero por encima del inicio inclinado; colisión y modelo coinciden. Cada pieza tiene ítem y drop independiente. Generador: `tools/create_school_split_raised_extras.py`; comprobación: `tools/check_school_split_raised_extras.py`; montaje: `tools/school_split_raised_extra_layout.json`. Se verifican 24 estados nuevos y continuidad con las cuatro piezas existentes. Sin compilar ni probar en Minecraft.
