1. **¿Por qué utilizamos @property en lugar de métodos tradicionales como getters y setters?**

Respuesta: El decorador @property se usa para permitir el acceso a los atributos de una clase de manera similar a un atributo, pero ejecutando código adicional (como validaciones o transformaciones) cuando se accede al atributo. Esto hace que el código sea más limpio y fácil de mantener, ya que no tienes que llamar a un método para obtener el valor, sino que puedes tratarlo como un atributo normal.

2. **¿Por qué la función math_operation acepta solo operaciones lambda?**

Respuesta: la función math_operation está diseñada para ser genérica, trabajando con cualquier operación matemática representada por una función lambda. Al aceptar funciones lambda como parámetros, math_operation puede realizar una variedad de operaciones matemáticas sin necesidad de definir cada operación de forma explícita.

3. **En el código de Library, si un libro tiene un ISBN que ya existe, ¿cómo manejamos esa situación?**

Respuesta: Podríamos agregar una verificación en el método add_book que revise si el ISBN del libro ya está presente antes de añadirlo. Esto se podría hacer con un bucle que recorra los libros y compare los ISBN, o usando un conjunto de ISBNs únicos para asegurar que no se repitan.

4. **¿Por qué el método borrow_book utiliza una variable is_borrowed para controlar si un libro está prestado?**

Respuesta: La variable is_borrowed se usa como una bandera para indicar si un libro está disponible o no. Cuando un libro se presta, cambiamos su valor a True, y cuando se devuelve, lo cambiamos a False. Es una forma sencilla de gestionar el estado del libro, asegurando que no se preste un libro que ya ha sido prestado. 

5.**En el método return_book, ¿por qué se verifica si el libro está prestado antes de devolverlo?**

Respuesta: En el método return_book, se verifica si el libro está marcado como prestado (is_borrowed) para asegurarse de que realmente se haya tomado prestado antes de intentar devolverlo. Esto es importante porque si un libro no está prestado, no tiene sentido realizar la operación de devolución. Esta verificación ayuda a evitar errores y proporciona una retroalimentación adecuada al usuario si intenta devolver un libro que no ha sido prestado.

6. **¿Por qué usamos el módulo uuid para generar IDs únicos para usuarios y libros, y qué implica esto en términos de aleatoriedad?**

Respuesta: El módulo uuid se usa para generar identificadores únicos universales (UUID) de manera aleatoria. En el caso de uuid4(), genera un UUID basado en un valor aleatorio, lo que hace muy improbable que dos UUIDs sean iguales, incluso si se generan en sistemas diferentes o en momentos diferentes. Al usar solo los primeros 8 caracteres del UUID, estamos asegurando que el ID sea único.

7. **¿Por qué usamos lower() para las búsquedas de libros por título o autor y qué sucede si hay caracteres especiales?**

Respuesta: Usamos lower() para hacer que la búsqueda sea insensible a mayúsculas y minúsculas, ya que no es necesario que coincidan exactamente las mayúsculas y minúsculas del texto ingresado con los títulos o autores almacenados. Sin embargo, esto no resuelve problemas con caracteres especiales, como acentos o caracteres no ASCII.