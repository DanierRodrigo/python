# =====================================================
# 1️⃣ CREACIÓN DE UN CONJUNTO
# =====================================================

asignaturas = {"Matemáticas", "Física", "Programación", "Matemáticas"}

# Observa que "Matemáticas" repetido NO se guarda dos veces
print(asignaturas)


# =====================================================
# 2️⃣ AÑADIR ELEMENTOS
# =====================================================

# 🔹 add() → Añade un elemento
asignaturas.add("Química")
print(asignaturas)

# 🔹 update() → Añade varios elementos
asignaturas.update(["Historia", "Inglés"])
print(asignaturas)


# =====================================================
# 3️⃣ ELIMINAR ELEMENTOS
# =====================================================

# 🔹 remove() → Elimina, da error si no existe
asignaturas.remove("Física")

# 🔹 discard() → Elimina, NO da error si no existe
asignaturas.discard("Biología")

# 🔹 pop() → Elimina un elemento aleatorio
elemento = asignaturas.pop()
print("Eliminado:", elemento)

# 🔹 clear() → Vacía el conjunto
# asignaturas.clear()


# =====================================================
# 4️⃣ OPERACIONES MATEMÁTICAS DE CONJUNTOS
# =====================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 🔹 Unión
print(A.union(B))
print(A | B)

# 🔹 Intersección
print(A.intersection(B))
print(A & B)

# 🔹 Diferencia
print(A.difference(B))
print(A - B)

# 🔹 Diferencia simétrica
print(A.symmetric_difference(B))
print(A ^ B)


# =====================================================
# 5️⃣ MÉTODOS RELACIONALES
# =====================================================

C = {1, 2}
D = {1, 2, 3, 4}

# 🔹 issubset() → ¿Está contenido?
print(C.issubset(D))

# 🔹 issuperset() → ¿Contiene a otro?
print(D.issuperset(C))

# 🔹 isdisjoint() → ¿No comparten elementos?
print(A.isdisjoint({7, 8}))


# =====================================================
# 6️⃣ PERTENENCIA
# =====================================================

print(3 in A)
print(10 in A)


# =====================================================
# 7️⃣ LONGITUD
# =====================================================

print(len(A))


# =====================================================
# 8️⃣ RECORRER UN CONJUNTO
# =====================================================

for elemento in A:
    print(elemento)

# ⚠️ No tiene orden garantizado


# =====================================================
# 9️⃣ CONVERSIÓN DE TIPOS
# =====================================================

# Lista a set (elimina duplicados)
lista = [1, 2, 2, 3, 4]
conjunto = set(lista)
print(conjunto)

# Set a lista
lista2 = list(conjunto)
print(lista2)


# =====================================================
# 🔟 CONJUNTO INMUTABLE (frozenset)
# =====================================================

# Un frozenset NO se puede modificar
fs = frozenset([1, 2, 3])
print(fs)

# fs.add(4)  # Esto daría error
