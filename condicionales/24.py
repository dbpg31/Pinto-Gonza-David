import os
os.system("cls")

vendido = int(input("Ingrese el monto total vendido por el vendedor: "))

sueldoBase = vendido * 0.10

if vendido > 5000:
    excesoventa = vendido - 5000
    bono= (excesoventa // 500) * 25
else:
    bono = 0

sueldototal = sueldoBase + bono

print("Sueldo base: S/.", sueldoBase)
print("Bono por venta en exceso: S/.", bono)
print("Sueldo neto : S/.", sueldototal)