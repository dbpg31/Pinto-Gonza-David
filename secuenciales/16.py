import os
os.system("cls")

sueldo = int( input("sueldo por hora = S/ "))
horas = int( input("horas trabajadas =  "))

sueldobase = sueldo * horas 

sueldoBruto = sueldobase * (1 + 0.20)
sueldoNeto = sueldoBruto * (1 - 0.10) 

print(f"sueldo bruto = S/ {sueldoBruto:.2f}")
print(f"sueldo neto = S/ {sueldoNeto:.2f}")

