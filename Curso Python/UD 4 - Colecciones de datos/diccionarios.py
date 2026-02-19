# =====================================================
# 1️⃣ CREACIÓN DE UN DICCIONARIO
# =====================================================

estudiante = {
    "nombre": "Carlos",
    "edad": 21,
    "carrera": "Ingeniería",
    "promedio": 8.9
}

print(estudiante)


# =====================================================
# 2️⃣ ACCESO A VALORES
# =====================================================

# Forma directa (puede dar error si no existe)
print(estudiante["nombre"])

# Método get() (NO da error si no existe)
print(estudiante.get("edad"))
print(estudiante.get("ciudad", "No especificada"))


# =====================================================
# 3️⃣ MODIFICAR VALORES
# =====================================================

estudiante["edad"] = 22
print(estudiante)


# =====================================================
# 4️⃣ AÑADIR NUEVOS ELEMENTOS
# =====================================================

estudiante["ciudad"] = "Madrid"
print(estudiante)


# =====================================================
# 5️⃣ ELIMINAR ELEMENTOS
# =====================================================

# 🔹 pop() → Elimina por clave y devuelve el valor
valor = estudiante.pop("promedio")
print("Eliminado:", valor)

# 🔹 popitem() → Elimina el último elemento añadido
clave, valor = estudiante.popitem()
print("Eliminado:", clave, valor)

# 🔹 del → Elimina por clave
# del estudiante["edad"]

# 🔹 clear() → Vacía el diccionario
# estudiante.clear()


# =====================================================
# 6️⃣ MÉTODOS IMPORTANTES
# =====================================================

# 🔹 keys() → Devuelve todas las claves
print(estudiante.keys())

# 🔹 values() → Devuelve todos los valores
print(estudiante.values())

# 🔹 items() → Devuelve clave y valor
print(estudiante.items())

# 🔹 update() → Actualiza o añade varios valores
estudiante.update({"edad": 23, "universidad": "UPM"})
print(estudiante)

# 🔹 copy() → Copia el diccionario
copia = estudiante.copy()
print(copia)

# 🔹 setdefault() → Devuelve valor si existe, si no lo crea
estudiante.setdefault("pais", "España")
print(estudiante)


# =====================================================
# 7️⃣ RECORRER UN DICCIONARIO
# =====================================================

# Solo claves
for clave in estudiante:
    print(clave)

# Claves y valores
for clave, valor in estudiante.items():
    print(clave, "→", valor)


# =====================================================
# 8️⃣ PERTENENCIA
# =====================================================

print("nombre" in estudiante)   # Busca en claves
print("Carlos" in estudiante)   # False (no busca en valores)


# =====================================================
# 9️⃣ LONGITUD
# =====================================================

print(len(estudiante))


# =====================================================
# 🔟 DICCIONARIOS POR COMPRENSIÓN
# =====================================================

# Crear diccionario con cuadrados
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)

# Con condición
pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares)
