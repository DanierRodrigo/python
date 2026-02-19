# =====================================================
# 1️⃣ CADENA BASE
# =====================================================

texto = "Python es genial"

print(texto)


# =====================================================
# 2️⃣ MÉTODO index()
# =====================================================

# Devuelve la posición donde comienza la subcadena
posicion = texto.index("es")
print("La palabra 'es' empieza en:", posicion)

# ⚠ Si no encuentra el texto → ValueError
# texto.index("Java")  # Esto daría error


# =====================================================
# 3️⃣ DIFERENCIA ENTRE index() Y find()
# =====================================================

# find devuelve -1 si no encuentra
print(texto.find("Java"))


# =====================================================
# 4️⃣ SLICING BÁSICO
# =====================================================

# Sintaxis:
# cadena[inicio:fin]

print(texto[0:6])    # "Python"
print(texto[7:9])    # "es"
print(texto[:6])     # Desde inicio hasta 5
print(texto[10:])    # Desde índice 10 hasta el final


# =====================================================
# 5️⃣ ÍNDICES NEGATIVOS
# =====================================================

print(texto[-6:])    # Últimos 6 caracteres
print(texto[-1])     # Última letra


# =====================================================
# 6️⃣ SLICING CON PASO (STEP)
# =====================================================

# Sintaxis:
# cadena[inicio:fin:paso]

print(texto[::2])    # De 2 en 2
print(texto[1::2])   # Empieza en 1, de 2 en 2


# =====================================================
# 7️⃣ INVERTIR CADENA
# =====================================================

print(texto[::-1])


# =====================================================
# 8️⃣ EXTRAER PALABRA USANDO index + slicing
# =====================================================

inicio = texto.index("genial")
fin = inicio + len("genial")

palabra = texto[inicio:fin]
print("Palabra extraída:", palabra)


# =====================================================
# 9️⃣ CONTROLAR ERROR DE index()
# =====================================================

try:
    print(texto.index("Java"))
except ValueError:
    print("La palabra no existe")
