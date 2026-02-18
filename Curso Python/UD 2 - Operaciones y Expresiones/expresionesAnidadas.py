total_compra = 150
es_vip = True

descuento = 0

if total_compra > 100:
    if es_vip:
        descuento = 0.20
    else:
        descuento = 0.10
else:
    if es_vip:
        descuento = 0.05
    else:
        descuento = 0

precio_final = total_compra * (1 - descuento)

print("Total compra:", total_compra)
print("¿Es cliente VIP?:", es_vip)
print("Descuento aplicado:", descuento * 100, "%")
print("Precio final:", precio_final)
