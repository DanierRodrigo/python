# range(inicio, fin, paso) el fin debe sumar 1 al número que queremos, el paso es el salto que da, en este caso de 2 en 2

for numero in range(0, 21, 2):
    print(numero)

# 1️⃣ Crear un range del 1 al 10
numeros = range(1, 11)

print("Tipo de numeros:", type(numeros))

# 2️⃣ Convertir a lista
lista_numeros = list(numeros)
print("Lista:", lista_numeros)

# 3️⃣ Convertir a tupla
tupla_numeros = tuple(numeros)
print("Tupla:", tupla_numeros)

# 4️⃣ Convertir a set
set_numeros = set(numeros)
print("Set:", set_numeros)

# 5️⃣ Recorrer con for
print("Recorriendo lista:")
for n in lista_numeros:
    print(n)

# 6️⃣ Acceder por índice (solo posible en lista o tupla)
print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# 7️⃣ Range con paso negativo (cuenta atrás)
cuenta_atras = list(range(10, 0, -1))
print("Cuenta atrás:", cuenta_atras)
