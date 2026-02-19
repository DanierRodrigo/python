# =====================================================
# 1️⃣ SALIDA DE DATOS - print()
# =====================================================

print("Bienvenido al programa")

# Podemos imprimir varios valores separados por coma
print("Hola", "mundo")

# Podemos cambiar el separador
print("Python", "es", "genial", sep="-")

# Podemos cambiar lo que aparece al final
print("Hola", end=" ")
print("Carlos")


# =====================================================
# 2️⃣ ENTRADA DE DATOS - input()
# =====================================================

# input() siempre devuelve STRING
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")

print("Tu nombre es:", nombre)
print("Tu edad es:", edad)


# =====================================================
# 3️⃣ CONVERSIÓN DE TIPOS
# =====================================================

# Como input devuelve texto, debemos convertir
edad = int(edad)

print("El año que viene tendrás:", edad + 1)


# =====================================================
# 4️⃣ FORMATEO DE CADENAS
# =====================================================

# 🔹 Forma 1: concatenación
print("Hola " + nombre + ", tienes " + str(edad) + " años.")

# 🔹 Forma 2: format()
print("Hola {}, tienes {} años.".format(nombre, edad))

# 🔹 Forma 3: f-strings (RECOMENDADO)
print(f"Hola {nombre}, tienes {edad} años.")


# =====================================================
# 5️⃣ ENTRADA DE VARIOS DATOS EN UNA SOLA LÍNEA
# =====================================================

datos = input("Introduce tres números separados por espacio: ")

# split() separa el texto
lista_datos = datos.split()

# Convertimos cada valor a entero
numeros = [int(x) for x in lista_datos]

print("Números:", numeros)
print("Suma:", sum(numeros))
