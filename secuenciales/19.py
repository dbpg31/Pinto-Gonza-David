import os
os.system("cls")

ventas = int( input("total de ventas = S/ "))

sueldobase = 500
sueldoBruto = sueldobase + (ventas * 0.09)
sueldoNeto = sueldoBruto  * (1 - 0.11)

print(f"sueldo Bruto = S/ {sueldoBruto:.2f}")
print(f"descuento = S/ {(sueldoBruto * 0.11):.2f}")
print(f"sueldo Bruto = S/ {sueldoNeto:.2f}")
