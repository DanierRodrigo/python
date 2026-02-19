# =====================================================
# 1️⃣ CREACIÓN DE UNA TUPLA
# =====================================================

estudiante = ("Carlos", 21, "Ingeniería", 8.9, 21)

# Nota:
# Puede contener diferentes tipos de datos
# Aquí tenemos: str, int, str, float, int


# =====================================================
# 2️⃣ ACCESO A ELEMENTOS (INDEXACIÓN)
# =====================================================

print(estudiante[0])  # "Carlos"
print(estudiante[2])  # "Ingeniería"

# Índices negativos (empiezan desde el final)
print(estudiante[-1])  # 21 (último elemento)


# =====================================================
# 3️⃣ SLICING (REBANADO)
# =====================================================

print(estudiante[0:2])   # ('Carlos', 21)
print(estudiante[:3])    # Desde inicio hasta índice 2
print(estudiante[1:])    # Desde índice 1 hasta el final


# =====================================================
# 4️⃣ MÉTODOS PROPIOS DE LAS TUPLAS
# =====================================================

# 🔹 count() → Cuenta cuántas veces aparece un valor
print(estudiante.count(21))  # 2

# 🔹 index() → Devuelve la posición de la primera aparición
print(estudiante.index("Ingeniería"))  # 2


# =====================================================
# 5️⃣ OPERADORES QUE FUNCIONAN CON TUPLAS
# =====================================================

# 🔹 Concatenación (+)
otra_tupla = ("España",)
nueva_tupla = estudiante + otra_tupla
print(nueva_tupla)

# 🔹 Repetición (*)
print(("Hola",) * 3)

# 🔹 Operador in (pertenencia)
print("Carlos" in estudiante)  # True
print("Ana" in estudiante)     # False


# =====================================================
# 6️⃣ LONGITUD
# =====================================================

print(len(estudiante))  # 5


# =====================================================
# 7️⃣ DESEMPAQUETADO (UNPACKING)
# =====================================================

nombre, edad, carrera, promedio, edad2 = estudiante

print(nombre)
print(edad)

# Desempaquetado con *
nombre, *datos_restantes = estudiante
print(datos_restantes)


# =====================================================
# 8️⃣ RECORRER UNA TUPLA
# =====================================================

for elemento in estudiante:
    print(elemento)


# =====================================================
# 9️⃣ CONVERSIÓN ENTRE TIPOS
# =====================================================

# Convertir tupla a lista
lista = list(estudiante)
print(lista)

# Convertir lista a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)


# =====================================================
# 🔟 INTENTAR MODIFICAR (ERROR)
# =====================================================

# Esto genera error porque la tupla es inmutable
# estudiante[1] = 25

# TypeError: 'tuple' object does not support item assignment
