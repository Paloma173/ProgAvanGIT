**PREGUNTAS**

**PREGUNTA 1**: Qué es el atributo TIME_FORMATS en la clase Time?
- Es una tupla que contiene los formatos de hora válidos ("AM", "PM", "24 HOURS"). Sirve para validar que el formato ingresado sea correcto.

**PREGUNTA 2**: Por qué usamos el método __assign_format en vez de asignar el formato directamente?
- Para asegurarnos de que el formato es válido y se almacene en mayúsculas, evitando errores de capitalización o formato incorrecto.

**PREGUNTA 3**: Qué hace el método set_time?
- Asigna las horas, minutos, segundos y el formato a la hora, validando que los valores estén en los rangos correctos para el formato especificado (AM/PM o 24 HOURS).
¿Cuál es la función del método from_string?

**PREGUNTA 4**: Convierte una cadena con formato "HH:MM
FORMAT" en un objeto Time, extrayendo y validando los valores de la hora desde la cadena.

**PREGUNTA 5**: Por qué usamos el decorador @classmethod en from_string y get_time_count?
- Porque estos métodos operan a nivel de clase. from_string crea un nuevo objeto de la clase, y get_time_count devuelve el número de objetos Time creados.

**PREGUNTA 6**: Qué verifica el método _is_valid_time?
- Comprueba que los valores de horas, minutos y segundos sean correctos según el formato de hora actual (1-12 para AM/PM, 0-23 para 24 HOURS).

**PREGUNTA 7**: Cómo funciona el menú en la función main?
- Presenta opciones al usuario para introducir o mostrar la hora, crear una hora desde una cadena o terminar el programa. Según la opción elegida, llama a los métodos correspondientes de la clase Time.






