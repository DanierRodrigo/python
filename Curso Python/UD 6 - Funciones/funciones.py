# =====================================================
# FUNCIÓN SIMPLE
# =====================================================

def saludar():
    print("Hola, bienvenido")

# Llamada a la función
saludar()

# =====================================================
# FUNCIÓN CON PARÁMETROS
# =====================================================

def saludar(nombre):  # nombre es parámetro
    print(f"Hola {nombre}")

saludar("Carlos")  # "Carlos" es argumento

# =====================================================
# FUNCIÓN CON MÚLTIPLES PARÁMETROS
# =====================================================

def sumar(a, b):
    print(a + b)

sumar(5, 3)

# =====================================================
# RETURN: SIN ESTO, LA FUNCION DEVUELVE NONE
# =====================================================

def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)


# =====================================================
# VALORES POR DEFECTO
# =====================================================

def saludar(nombre="Invitado"):
    print(f"Hola {nombre}")

saludar()          # Usa valor por defecto
saludar("Ana")     # Sobrescribe

# =====================================================
# ARGUMENTOS POR POSICIÓN Y NOMBRE
# =====================================================

def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

# Por posición
presentar("Carlos", 21)

# Por nombre (keyword arguments)
presentar(edad=21, nombre="Carlos")

# =====================================================
# ARGUMENTOS INDETERMINADOS   *args → TUPLA
# =====================================================

def sumar_todo(*numeros):
    print(type(numeros))  # Es tupla
    return sum(numeros)

print(sumar_todo(1, 2, 3, 4))

# =====================================================
# ARGUMENTOS INDETERMINADOS   **kwargs → DICCIONARIO
# =====================================================

def mostrar_datos(**datos):
    print(type(datos))  # Es diccionario
    for clave, valor in datos.items():
        print(clave, "→", valor)

mostrar_datos(nombre="Carlos", edad=21)

# =====================================================
# COMBINACION COMPLETA
# =====================================================

def ejemplo(a, b, *args, opcion=True, **kwargs):
    print(a, b)
    print(args)
    print(opcion)
    print(kwargs)

ejemplo(1, 2, 3, 4, opcion=False, nombre="Ana")

# =====================================================
# FUNCIONES LAMBDA
# =====================================================

# Forma normal
def cuadrado(x):
    return x**2

# Lambda
cuadrado = lambda x: x**2

print(cuadrado(5))

# Muy usadas
numeros = [1, 2, 3]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# =====================================================
# DOCUMENTACIÓN (DOCSTRING)
# =====================================================

def sumar(a, b):
    """
    Esta función suma dos números
    Parámetros:
    a → número
    b → número
    Devuelve:
    Suma de ambos
    """
    return a + b

help(sumar)

# =====================================================
# ÁMBITO DE VARIABLES LOCAL - GLOBAL
# =====================================================

x = 10  # Variable global

def funcion():
    x = 5  # Variable local
    print(x)

funcion()
print(x)

