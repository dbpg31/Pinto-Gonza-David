import os
os.system("cls")

unidades = int( input("unidades = "))
precioBase = int( input("precio = "))

venta = unidades * precioBase
 
venta1 = venta * (1 - 0.15)
ventafinal = venta1 * (1 - 0.15)

descuento1 = venta * 0.15 
descuent2 = venta1 * 0.15
descuentototal = descuento1 + descuent2

print(f"venta = S/ {venta:.2f}")
print(f"descuento total = S/ {descuentototal:.2f}")
print(f"venta final = S/ {ventafinal:.2f}")
