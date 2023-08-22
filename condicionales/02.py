import os

os.system("cls")

unidades = int( input("unidades = "))
importe = unidades * 20

descuento = 0.14 * importe
if importe <= 500 : descuento = 0.12 * importe
elif importe > 700 : descuento = 0.16 * importe

ncaramelos = 10
if unidades <= 50 : ncaramelos = 5
elif unidades > 100 : ncaramelos = 15

print(f"importe dew compra = S/ {importe:.2f}")
print(f"descuento = S/ {descuento:.2f}")
print(f"total a pagar = S/ {(importe - descuento):.2f}")
print(f"caramelos =  {ncaramelos:.2f}")

