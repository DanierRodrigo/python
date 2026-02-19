# =====================================================
# CAPTURA BÁSICA DE ERRORES
# =====================================================

# try - catch

try:
    numero = int(input("Introduce un número: "))
    print(10 / numero)

except:
    print("Ha ocurrido un error")

# Manejo manual de errores

try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(resultado)

except ValueError:
    print("Debes introducir un número válido")

except ZeroDivisionError:
    print("No se puede dividir entre cero")

# Capturar el error como variable

try:
    x = int("hola")

except ValueError as e:
    print("Error detectado:", e)

# Multiples excepciones en una sola línea

try:
    x = int(input())
    print(10 / x)

except (ValueError, ZeroDivisionError):
    print("Error en los datos")


# Clausula else

try:
    numero = int(input("Número: "))
except ValueError:
    print("No válido")
else:
    print("Correcto, número introducido:", numero)


# =====================================================
# CLAUSULA FINALLY. Se ejecuta siempre haya error o no
# =====================================================

try:
    archivo = open("datos.txt")
    contenido = archivo.read()

except FileNotFoundError:
    print("Archivo no encontrado")

finally:
    print("Fin del programa")

# =====================================================
# LANZAR ERRORES MANUALMENTE
# =====================================================

edad = int(input("Edad: "))

if edad < 0:
    raise ValueError("La edad no puede ser negativa")

# =====================================================
# CREAR EXEPCIONES PERSONALIZADAS
# =====================================================

class EdadInvalidaError(Exception):
    pass

edad = int(input("Edad: "))

if edad < 0:
    raise EdadInvalidaError("Edad negativa no permitida")

# =====================================================
# ASSERT (Validaciones rápidas)
# =====================================================

x = 5
assert x > 0, "El número debe ser positivo"




