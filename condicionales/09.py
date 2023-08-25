import os
os.system("cls")

codigo = int( input("codigo = "))
unidades = int( input("unidades = "))

if codigo == 101 : precio = 17
elif codigo == 102 : precio = 25
elif codigo == 103 : precio = 16
elif codigo == 104 : precio = 27

venta = unidades * precio 

if unidades <= 10 : descuento = venta * 0.05
elif unidades > 10 and unidades <= 20 : descuento = venta * 0.08
elif unidades > 20 and unidades <= 30 : descuento = venta * 0.10
elif unidades > 30 : descuento = venta * 0.13

print(f"importe de compra = S/{venta:.2f}")
print(f"importe de descuento = S/{descuento:.2f}")
print(f"importe neto a pagar = S/{(venta - descuento):.2f}")
