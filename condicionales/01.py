import os
os.system("cls")

unidades = int( input("unidades : "))

precio = 0
if unidades <= 25 : precio = 27
elif unidades > 25 and unidades <= 50 : precio = 25
elif unidades > 50 : precio = 23

compra = unidades * precio 

descuento = 0.05 * compra
if unidades > 50 : descuento = 0.15 * compra

print(f"importe de compra = S/ {compra:.2f}")
print(f"descuento = S/ {descuento:.2f}")
print(f"total a pagar = S/ {(compra - descuento):.2f} ")



