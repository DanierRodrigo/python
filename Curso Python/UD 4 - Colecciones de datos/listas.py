# =====================================================
# 1️⃣ CREACIÓN DE UNA LISTA
# =====================================================

estudiante = ["Carlos", 21, "Ingeniería", 8.9, 21]

# A diferencia de las tuplas, esta SÍ se puede modificar


# =====================================================
# 2️⃣ ACCESO A ELEMENTOS (INDEXACIÓN)
# =====================================================

print(estudiante[0])   # "Carlos"
print(estudiante[-1])  # 21 (último elemento)


# =====================================================
# 3️⃣ MODIFICACIÓN (MUTABILIDAD)
# =====================================================

estudiante[1] = 22   # Cambiamos la edad
print(estudiante)


# =====================================================
# 4️⃣ SLICING (REBANADO)
# =====================================================

print(estudiante[0:2])
print(estudiante[:3])
print(estudiante[1:])


# =====================================================
# 5️⃣ MÉTODOS DE LAS LISTAS
# =====================================================

# 🔹 append() → Añade un elemento al final
estudiante.append("España")
print(estudiante)

# 🔹 insert() → Inserta en una posición específica
estudiante.insert(1, "Masculino")
print(estudiante)

# 🔹 extend() → Añade varios elementos
estudiante.extend(["Python", "Matemáticas"])
print(estudiante)

# 🔹 remove() → Elimina el primer valor que coincida
estudiante.remove(21)
print(estudiante)

# 🔹 pop() → Elimina por índice y lo devuelve
elemento_eliminado = estudiante.pop(0)
print(elemento_eliminado)
print(estudiante)

# 🔹 clear() → Vacía la lista
# estudiante.clear()

# 🔹 index() → Devuelve posición
print(estudiante.index("Ingeniería"))

# 🔹 count() → Cuenta apariciones
print(estudiante.count(21))

# 🔹 sort() → Ordena la lista (solo si son del mismo tipo)
numeros = [5, 1, 8, 3]
numeros.sort()
print(numeros)

# 🔹 reverse() → Invierte el orden
numeros.reverse()
print(numeros)

# 🔹 copy() → Copia la lista
copia = numeros.copy()
print(copia)


# =====================================================
# 6️⃣ OPERADORES
# =====================================================

# Concatenación
lista1 = [1, 2]
lista2 = [3, 4]
print(lista1 + lista2)

# Repetición
print([1, 2] * 3)

# Pertenencia
print(2 in lista1)


# =====================================================
# 7️⃣ LONGITUD
# =====================================================

print(len(estudiante))


# =====================================================
# 8️⃣ RECORRER LISTA
# =====================================================

# Forma 1
for elemento in estudiante:
    print(elemento)

# Forma 2 (con índice)
for i in range(len(estudiante)):
    print(i, estudiante[i])


# =====================================================
# 9️⃣ LISTAS POR COMPRENSIÓN
# =====================================================

# Crear lista de cuadrados
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

# Con condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)


# =====================================================
# 🔟 CONVERSIÓN DE TIPOS
# =====================================================

# Convertir tupla a lista
tupla = (1, 2, 3)
lista = list(tupla)
print(lista)

# Convertir lista a tupla
tupla2 = tuple(lista)
print(tupla2)
