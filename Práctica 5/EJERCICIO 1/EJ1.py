# Decorador que registra el nombre de la operación, las entradas y el resultado
def operation_logger(func):
    def wrapper(*args, **kwargs):
        # Registrar la operación y sus entradas
        print(f"Operación: {func.__name__}")
        print(f"Entradas: {args} {kwargs}")
        
        try:
            # Ejecutar la operación y obtener el resultado
            result = func(*args, **kwargs)
            # Registrar el resultado
            print(f"Resultado: {result}")
        except Exception as e:
            # Manejar errores si ocurre alguno (por ejemplo, división por cero)
            print(f"Error: {e}")
            result = None
        
        return result
    return wrapper

# Funciones lambda para operaciones matemáticas básicas
add = lambda *args: sum(args)
subtract = lambda a, b: a - b
multiply = lambda *args: 1 if len(args) == 0 else args[0] * multiply(*args[1:])
divide = lambda a, b: a / b if b != 0 else "Error: División por cero"

# Función que usa la operación y los argumentos dados
@operation_logger
def math_operation(operation, *args, **kwargs):
    return operation(*args, **kwargs)

# Pruebas con las operaciones y entradas indicadas
print("\nResultado de math_operation(add, 5, 3):")
math_operation(add, 5, 3)

print("\nResultado de math_operation(subtract, 10, 4):")
math_operation(subtract, 10, 4)

print("\nResultado de math_operation(multiply, 2, 6):")
math_operation(multiply, 2, 6)

print("\nResultado de math_operation(divide, 15, 3):")
math_operation(divide, 15, 3)

print("\nResultado de math_operation(divide, 10, 0):")
math_operation(divide, 10, 0)

print("\nResultado de math_operation(add, 1, 2, 3, 4, 5):")
math_operation(add, 1, 2, 3, 4, 5)
