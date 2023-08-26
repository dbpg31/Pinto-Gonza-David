import os
os.system("cls")

numero = int(input("cantidad de docenas : "))
precio = int(input("precio por docena = S/ "))

venta = numero * precio

if numero >= 6 : descuento = venta * 0.15
elif numero < 6 : descuento = venta * 0.10

lapiceros = 0

if numero >= 30 : lapiceros = int((numero/3) * 2)

print(f"monto de compra = S/ {venta:.2f}")
print(f"descuento = S/ {descuento:.2f}")
print(f"lapiceros = {lapiceros:.2f}")
