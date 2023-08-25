import os
os.system("cls")

unidadA = int( input("unidades de A : "))
unidadB = int( input("unidades de B : "))

ventaA = unidadA * 25 

if unidadA > 50 : descuentoA = ventaA * 0.15
else : descuentoA = 0
ventaB = unidadB * 30 

if unidadB > 60 : descuentoB = ventaB * 0.10
else : descuentoB = 0


print(f"importe bruto = S/ {(ventaA + ventaB):.2f}")
print(f"importe de descuento = S/ {(descuentoA + descuentoB):.2f}")
print(f"neto a pagar = S/ {((ventaA - descuentoA) + (ventaB - descuentoB)):.2f}")