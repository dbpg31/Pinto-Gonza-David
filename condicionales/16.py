import os
os.system("cls")

ingreso = int(input("ingreso mensual = S/ "))
costoCasa = int(input("costo de la casa  = S/ "))

if ingreso < 1250 : cuotainicial = costoCasa * 0.15 ; cuota = (costoCasa - cuotainicial)/120
elif ingreso >= 1250 : cuotainicial = costoCasa * 0.30 ; cuota = (costoCasa - cuotainicial)/75

print(f"cuota inicial = S/{cuotainicial:.2f}")
print(f"cuota = S/{cuota:.2f}")


