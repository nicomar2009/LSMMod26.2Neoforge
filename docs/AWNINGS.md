# Toldos conservados y soportes finos

Solo se registran playground_awning y elementary_playground_awning, además del bloque de soporte awning_support. Se eliminan el toldo base awning y sus dieciséis colores: registros de bloque/ítem, modelos, estados, texturas, loot y traducciones. La geometría compartida vive ahora en los modelos de playground_awning; elementary_playground_awning la hereda con su propia tela. El tipo de entidad compartido permanece para gestionar ambos toldos y el soporte.

Cada celda de awning_support contiene tres varillas paralelas de 1×1 px, en x2..3, x7.5..8.5 y x13..14, que recorren todo el bloque hasta sus dos caras de unión. Dos líneas transversales de 1×1 px en z0..1 y z15..16 sirven de anclaje junto a la pared y al borde del toldo. Todo está a y13..14, coincidiendo con la altura de fijación de la tela. Mantiene el metal del soporte, ancho seleccionable 1..16 y el sistema de parejas de soportes. El modelo de inventario muestra las mismas líneas finas.

La colisión contiene solo las cinco varillas; selección simple mediante SimpleBlockOutline, independiente de la colisión y con perfiles precalculados para ambos ejes. Las telas conservan sus pendientes, colores, colocación, límites y retirada conjunta.

Generador tools/create_awning_assets.py; manifiesto tools/awning_variants.json; validación tools/check_awning_assets.py: 4624 estados de tela, herencia de modelos sin referencias eliminadas y 1024 estados del soporte. Retira los toldos base/de colores de los mundos antes de actualizar: esos IDs ya no existen. Sin compilación ni prueba dentro de Minecraft.
