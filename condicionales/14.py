import os
os.system("cls")

numero = int( input("número de tarjeta : "))
venta = int( input("monto  de compra : "))


if numero >= 100 and (numero % 2) == 0 : descuento = venta * 0.15
else : descuento = venta * 0.05

print(f"numero de la tarjeta = {numero}")
print(f"descuento = S/ {descuento:.2f}")
print(f"monto de compra  = S/ {(venta - descuento):.2f}")

