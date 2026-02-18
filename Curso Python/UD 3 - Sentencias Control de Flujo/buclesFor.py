# Variable acumuladora (empieza en 0)
suma = 0

# El bucle for recorre los números del 1 al 5
# range(1, 6) significa: empieza en 1 y termina en 5
for numero in range(1, 6):
    
    # En cada vuelta del bucle se suma el número actual
    suma += numero
    
    # Mostramos lo que va pasando en cada iteración
    print("Número actual:", numero)
    print("Suma parcial:", suma)
    print("-----------")

# Cuando termina el bucle mostramos el resultado final
print("Suma total:", suma)
