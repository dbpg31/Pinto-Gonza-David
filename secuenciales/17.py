import os
os.system("cls")

donacion = int(input("donacion anual = S/ "))

salud = donacion * 0.25
comedor = donacion * 0.35
escuela = donacion * 0.25
asilo = donacion * 0.15

print(f"centro de salud = S/ {salud:.2f}")
print(f"comedor infantil = S/ {comedor:.2f}")
print(f"escuela infantil = S/ {escuela:.2f}")
print(f"asilo de ancianos = S/ {asilo:.2f}")
