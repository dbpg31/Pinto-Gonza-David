import os
os.system("cls")

sueldobasico = 600
monto = int(input("Ingrese el monto total vendido : "))

comision = monto * 0.15
sueldoBruto = sueldobasico + comision

if sueldoBruto > 1800:
    descuento = sueldoBruto * 0.10
else:
    descuento = sueldoBruto * 0.05

neto = sueldoBruto - descuento

if monto > 1000:
    polos = 3
else:
    polos = 1

print("Sueldo bruto: S/.", sueldoBruto)
print("Descuento: S/.", descuento)
print("Sueldo neto: S/.", neto)
print("Número de polos obsequiados: ", polos)



