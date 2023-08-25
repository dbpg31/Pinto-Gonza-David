import os
os.system("cls")

horas=int(input("horas trabajadas : "))
cartegoria = input("categoria : ")

if cartegoria == "A": pago = 21
elif cartegoria == "B" : pago = 19.50 
elif cartegoria == "C" : pago = 17 
elif cartegoria == "D" : pago = 15.5

sueldo = pago * horas

if sueldo > 2500 : descuento = sueldo * 0.20
elif sueldo <= 2500 : descuento = sueldo * 0.15

print(f"sueldo bruto = S/ {sueldo:.2f}")
print(f"descuento = S/ {descuento:.2f}")
print(f"sueldo bruto = S/ {(sueldo - descuento):.2f}")
