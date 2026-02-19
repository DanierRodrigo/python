# =====================================================
# STRINGS EN PYTHON — RECORDATORIO
#Son inmutables
#Se definen con comillas simples o dobles
# =====================================================

texto = "hola mundo"

# =====================================================
# CAPITALIZE (PRIMERA LETRA EN MAYÚSCULA)
# =====================================================

texto = "hola mundo"
print(texto.capitalize())  
# "Hola mundo"

# =====================================================
# LOWER (CONVIERTE EL STRING A MIÚSCULAS)
# =====================================================

print("HOLA".lower())
# "hola"

# =====================================================
# UPPER (CONVIERTE EL STRING A MAYÚSCULAS)
# =====================================================

print("hola".upper())
# "HOLA"

# =====================================================
# SWAPCASE (INVIERTE MAYÚSCULAS Y MINÚSCULAS)
# =====================================================

print("Hola Mundo".swapcase())
# "hOLA mUNDO"

# =====================================================
# TITLE (PRIMERA LETRA DE CADA PALABRA EN MAYÚSCULAS)
# =====================================================

print("hola mundo python".title())
# "Hola Mundo Python"

# =====================================================
# CENTER (CENTRA EL TEXTO, RECIBE COMO PARÁMETROS ANCHO Y RELLENO)
# =====================================================

print("Python".center(20))
print("Python".center(20, "*"))

# =====================================================
# LJUST (ALINEA A LA IZQUIERDA, RECIBE COMO PARÁMETROS ANCHO Y RELLENO)
# =====================================================

print("Python".ljust(15, "-"))

# =====================================================
# RJUST (ALINEA A LA DERECHA, RECIBE COMO PARÁMETROS ANCHO Y RELLENO)
# =====================================================

print("Python".rjust(15, "-"))

# =====================================================
# ZFILL (RELLENA CON CEROS A LA IZQUIERDA)
# =====================================================

print("42".zfill(5))
# "00042"

# =====================================================
# COUNT (CUENTA APARICIONES)
# =====================================================

texto = "banana"
print(texto.count("a"))
# 3

# =====================================================
# FIND (DEVUELVE POSICIÓN O -1 SI NO EXISTE)
# =====================================================

print("hola mundo".find("mundo"))

# =====================================================
# STARTSWITH (PREFIJO)
# =====================================================

print("Python".startswith("Py"))

# =====================================================
# ENDSWITH (SUFIJO)
# =====================================================

print("archivo.txt".endswith(".txt"))

# =====================================================
# ISALNUM (SOLO LETRAS Y NÚMEROS)
# =====================================================

print("abc123".isalnum())

# =====================================================
# ISALPHA (SOLO LETRAS)
# =====================================================

print("Hola".isalpha())

# =====================================================
# ISNUMERIC (SOLO LETRAS)
# =====================================================

print("123".isnumeric())

# =====================================================
# ISDECIMAL (SOLO NÚMEROS DECIMALES)
# =====================================================

print("123".isdecimal())

# =====================================================
# ISDIGIT (SIMILAR A ISNUMERIC, QUE ES MÁS RESTRICTIVO)
# =====================================================

print("123".isdigit())

# =====================================================
# ISSPACE (SOLO ESPACIOS)
# =====================================================

print("   ".isspace())

# =====================================================
# ISTITLE (PRIMERA LETRA DE CADA PALABRA EN MAYÚSCULA)
# =====================================================

print("Hola Mundo".istitle())

# =====================================================
# REPLACE (VIEJO, NUEVO)
# =====================================================

print("Hola mundo".replace("mundo", "Python"))

# =====================================================
# STRIP (ELIMINA ESPACIOS EXTREMOS)
# =====================================================

print("   hola   ".strip())

# =====================================================
# LSTRIP (ELIMINA ESPACIOS EXTREMOS A LA IZQUIERDA)
# =====================================================

print("   hola".lstrip())

# =====================================================
# RTRIP (ELIMINA ESPACIOS EXTREMOS)
# =====================================================

print("hola   ".rstrip())

# =====================================================
# SPLIT (DIVIDE EN LISTA)
# =====================================================

texto = "uno,dos,tres"
print(texto.split(","))

# =====================================================
# SPLITLINES (DIVIDE POR SALTOS DE LÍNEA)
# =====================================================

texto = "hola\nmundo"
print(texto.splitlines())

# =====================================================
# JOIN (UNE ELEMENTOS CON SEPARADOR)
# =====================================================

lista = ["Python", "es", "genial"]
print(" ".join(lista))

# =====================================================
# PARTITION (DIVIDE EN 3 PARTES)
# =====================================================

texto = "clave=valor"
print(texto.partition("="))

# =====================================================
# ORD (DEVUELVE CÓDIGO UNICODE DE UN CARÁCTER)
# =====================================================

print(ord("A"))

# 65


