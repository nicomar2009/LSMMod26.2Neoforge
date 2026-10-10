# Escudo del colegio 4×4

`school_shield` coloca con un solo ítem 16 piezas horizontales en X/Z, de 8 píxeles de altura. La celda elegida es el controlador (columna 1, fila 1); en un tamaño par está en una de las cuatro posiciones centrales. La huella se extiende una celda a un lado y dos al otro, según la orientación del jugador. Se comprueba todo el espacio y los permisos antes de colocar. Romper una pieza retira el conjunto y entrega un solo ítem; los fragmentos no tienen drops propios.

Textura de 64×64 dividida en dieciséis PNG 16×16: fondo original de classroom_floor, borde dorado y escudo rojo/blanco/negro redibujado a píxeles siguiendo la referencia inmediatamente debajo de la línea amarilla. No incluye el encabezado ni el texto del colegio. Paleta limitada, sin suavizado, con detalles discretos para la estética vanilla. Los lados y la cara inferior usan classroom_floor. Colisión y selección de slab inferior, sin partes elevadas ni ampliación manual.

Se conserva el ID school_shield. Los montajes antiguos de 3×3 deben retirarse y recolocarse para obtener el nuevo conjunto. Los archivos originales lsm1..9 y sus proyectos Blockbench siguen disponibles como referencia; ya no son los modelos usados por school_shield.

Generador: tools/create_school_shield_floor_assets.py. Verificación: tools/check_school_shield.py (64 estados, alturas, ensamblado de texturas, transformaciones de las cuatro orientaciones y controlador/drop únicos). Preview: previews/school_shield_4x4.png. Sin compilación ni prueba dentro de Minecraft.
