import os
os.system("cls")

sueldobruto = int(input("Ingrese el sueldo bruto del empleado: "))
cantidadhijos = int(input("Ingrese la cantidad de hijos del empleado: "))

if cantidadhijos > 0:
    bonificacion = (sueldobruto * 0.125) + (cantidadhijos * 40)
else:
    bonificacion = sueldobruto * 0.10

neto = sueldobruto + bonificacion

print("Bonificación: S/.", bonificacion)
print("Sueldo neto a pagar: S/.",neto)



