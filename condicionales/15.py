import os
os.system("cls")

venta = int(input("total vendido = "))

sueldobase = 250

if venta <= 5000 : comision = 0.05 ; sueldo = sueldobase + (venta * 0.05)
elif venta > 5000 and venta <= 10000 : comision = 0.08 ; sueldo = sueldobase + (venta * 0.08)
elif venta > 10000 and venta <= 20000 : comision = 0.10 ; sueldo = sueldobase + (venta * 0.10)
elif venta > 20000 : comision = 0.15 ; sueldo = sueldobase + (venta * 0.15)

if sueldo > 3500 : descuento = sueldo * 0.15
else : descuento = sueldo * 0.08

print(f"sueldo bruto = S/ {sueldo:.2f}")
print(f"comisión = S/ {(comision * venta):.2f}")
print(f"descuento = S/ {descuento:.2f}")
print(f"sueldo neto = S/ {(sueldo - descuento):.2f}")


