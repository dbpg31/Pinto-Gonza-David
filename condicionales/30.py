import os
os.system("cls")

cuota = int(input("cuota = S/ "))
dia = int(input("dia de pago  : "))


if dia <= 10 and (cuota * 0.02) > 5 : descuento = -0.02 * cuota
elif dia <= 10 and (cuota * 0.02) <= 5 : descuento = -5
elif dia > 10 and dia <= 20 : descuento = 0


if dia > 20 and (cuota * 0.03) > 10 : descuento = 0.03 * cuota
elif dia > 20 and (cuota * 0.03) <= 10 : descuento = 10

print(f"cuota a pagar = S/ {(cuota + descuento):.2f}")
print(f"descuento = S/ {(descuento):.2f}")

