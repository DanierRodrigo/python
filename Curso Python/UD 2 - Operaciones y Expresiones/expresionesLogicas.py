nota1 = 8
nota2 = 6
nota3 = 7

edad = 22
familia_numerosa = False

precio_matricula = 1000

# 1️⃣ Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# 2️⃣ Condición para beca
beca = (promedio >= 7 and edad < 25) or familia_numerosa

# 3️⃣ Aplicar descuento
if beca:
    precio_matricula *= 0.5

# 4️⃣ Mostrar resultados
print("Promedio:", promedio)
print("¿Tiene beca?:", beca)
print("Precio final:", precio_matricula)
