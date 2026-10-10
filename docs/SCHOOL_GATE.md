# Portón doble 6×4

`school_gate` coloca 24 celdas de ancho 6 y alto 4 mediante un ítem. Conserva el plano central de 2 px de profundidad, z7..9. Dos hojas de 48 px se encuentran entre las columnas 2 y 3, con una separación de 0,25 px. El controlador sigue siendo columna 2, fila 0, profundidad 0: al ser un ancho par, es una de las dos celdas centrales inferiores. Apoyos en ambos extremos (columnas 0 y 5).

Las hojas abren juntas 90 grados mediante clic derecho. El recorrido de cada hoja ocupa 48 px desde el pivote: tramos de 8, 16, 16 y 8 px en cuatro celdas de profundidad. Se comprueban espacio, permisos, límites, chunks e interferencias antes de moverlas. La última celda tiene solo medio bloque de geometría, también en colisión. El plano vacío conserva las celdas de control cuando está abierto. Romper cualquier pieza retira el portón y entrega un solo ítem.

Texturas 16×16 por celda, conjunto 96×64. Metal marrón oscuro, bastidores, manijas centrales y malla superior transparente; estilo pixelado y paleta compatible con las barandas existentes. school_gate_edge conserva su textura. Ítem actualizado al conjunto completo. Los portones antiguos 5×3 deben retirarse y recolocarse antes de actualizar el montaje.

Generador tools/create_school_gate_assets.py; verificación tools/check_school_gate_assets.py. Comprueba 768 estados, cuatro orientaciones, dimensiones abiertas/cerradas, preservación del dibujo al girar las hojas, transformaciones de control y drop único. Selección simple separada de la colisión física. Sin compilar ni probar dentro de Minecraft.
