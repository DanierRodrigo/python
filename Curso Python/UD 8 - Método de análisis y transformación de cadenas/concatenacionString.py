# =====================================================
# 1️⃣ DATOS INICIALES
# =====================================================

nombre = "Carlos"
edad = 21
ciudad = "Madrid"

# =====================================================
# 2️⃣ CONCATENACIÓN CON +
# =====================================================

# ⚠ Necesitamos convertir números a string
mensaje1 = "Hola, me llamo " + nombre + ", tengo " + str(edad) + " años y vivo en " + ciudad + "."
print(mensaje1)

# Problema: poco legible y requiere conversiones


# =====================================================
# 3️⃣ CONCATENACIÓN CON f-STRINGS (RECOMENDADO)
# =====================================================

mensaje2 = f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}."
print(mensaje2)

# Más limpio, moderno y profesional


# =====================================================
# 4️⃣ CONCATENACIÓN CON .format()
# =====================================================

mensaje3 = "Hola, me llamo {}, tengo {} años y vivo en {}.".format(nombre, edad, ciudad)
print(mensaje3)

# Alternativa válida, pero menos usada hoy


# =====================================================
# 5️⃣ CONCATENACIÓN CON join()
# =====================================================

partes = ["Hola,", "me", "llamo", nombre + ",", "vivo", "en", ciudad + "."]
mensaje4 = " ".join(partes)
print(mensaje4)

# join() es útil cuando trabajamos con listas


# =====================================================
# 6️⃣ CONCATENACIÓN CON +=
# =====================================================

mensaje5 = "Hola, "
mensaje5 += "me llamo "
mensaje5 += nombre
mensaje5 += "."
print(mensaje5)

# Útil para construir texto progresivamente


# =====================================================
# 7️⃣ REPETICIÓN CON *
# =====================================================

separador = "-" * 30
print(separador)


# =====================================================
# 8️⃣ CONCATENACIÓN AUTOMÁTICA ENTRE STRINGS
# =====================================================

mensaje6 = "Hola " "mundo"
print(mensaje6)

# Python une automáticamente strings contiguos


# =====================================================
# 9️⃣ CONCATENACIÓN CON print()
# =====================================================

print("Hola,", nombre, "tienes", edad, "años")

# print añade espacios automáticamente
