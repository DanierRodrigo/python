#Ejemplo operadores lógicos

edad = 20
tiene_carnet = True

# Operador AND (ambas condiciones deben cumplirse)
if edad >= 18 and tiene_carnet:
    print("Puede conducir")

# Operador OR (al menos una condición debe cumplirse)
if edad < 18 or not tiene_carnet:
    print("No puede conducir")

# Operador NOT (invierte el valor lógico)
es_mayor = edad >= 18
print("¿No es mayor de edad?", not es_mayor)
