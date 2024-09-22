

#Crear una funcion de descuento
def calular_descuento(monto_total, porcentaje):

    descuento  = monto_total * porcentaje/100
    return descuento
 

monto_total = 3500
descuento = calular_descuento(monto_total = 1300, porcentaje = 13)
print(f"Monto total de {monto_total}:")
print(f"descuento", {descuento})

print("___________________________________________")
monto_total2 = 2000
descuento = 25
descuento2 = calular_descuento(monto_total2, descuento)
print(f"Monto total de {monto_total2}: ")
print(f"descuento", {descuento2})