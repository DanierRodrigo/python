# Variable contador (empieza en 1)
contador = 1

# El bucle se ejecuta MIENTRAS la condición sea verdadera
while contador <= 5:
    
    # Se muestra el valor actual
    print("Contador:", contador)
    
    # Es MUY importante modificar la variable
    # Si no, el bucle sería infinito
    contador += 1

# Cuando la condición deja de cumplirse, el bucle termina
print("Fin del programa")
