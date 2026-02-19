# =====================================================
# 1️⃣ DATOS DEL PRODUCTO
# =====================================================

nombre = "Portátil"
precio = 899.9567
cantidad = 3
descuento = 0.15

total = precio * cantidad


# =====================================================
# 2️⃣ CONCATENACIÓN (NO RECOMENDADA)
# =====================================================

print("Producto: " + nombre + " Precio: " + str(precio))


# =====================================================
# 3️⃣ MÉTODO format()
# =====================================================

print("Producto: {} | Precio: {:.2f}€ | Cantidad: {}".format(nombre, precio, cantidad))

# {:.2f} → 2 decimales


# =====================================================
# 4️⃣ F-STRINGS (RECOMENDADO)
# =====================================================

print(f"Producto: {nombre}")
print(f"Precio unitario: {precio:.2f}€")
print(f"Cantidad: {cantidad}")
print(f"Total: {total:.2f}€")


# =====================================================
# 5️⃣ CONTROL DE DECIMALES
# =====================================================

print(f"Precio con 1 decimal: {precio:.1f}")
print(f"Precio con 3 decimales: {precio:.3f}")


# =====================================================
# 6️⃣ PORCENTAJES
# =====================================================

print(f"Descuento: {descuento:.0%}")
print(f"Descuento exacto: {descuento:.2%}")


# =====================================================
# 7️⃣ ALINEACIÓN DE TEXTO
# =====================================================

print(f"{nombre:<15} | Alineado izquierda")
print(f"{nombre:>15} | Alineado derecha")
print(f"{nombre:^15} | Centrado")


# =====================================================
# 8️⃣ RELLENO CON CARACTERES
# =====================================================

print(f"{nombre:*^20}")   # Centrado con *
print(f"{cantidad:0>5}")  # Relleno con ceros


# =====================================================
# 9️⃣ ANCHO DE CAMPO Y ESPACIADO
# =====================================================

numero = 42
print(f"{numero:5}")     # Ancho mínimo 5
print(f"{numero:05}")    # Relleno con ceros


# =====================================================
# 🔟 FORMATO DE NÚMEROS GRANDES
# =====================================================

numero_grande = 1000000
print(f"{numero_grande:,}")   # Separador miles
print(f"{numero_grande:_}")   # Separador con _
