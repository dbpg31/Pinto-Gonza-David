import os
os.system("cls")

donacion = int( input("donación = "))

if donacion >= 10000 : salud = donacion * 0.30 ; comedor = donacion * 0.50 ; bolsa = donacion * 0.20
elif donacion < 10000 : salud = donacion * 0.25 ; comedor = donacion * 0.60 ; bolsa = donacion * 0.15

print(f"centro de salud = S/ {salud:.2f}")
print(f"comedor de niños = S/ {comedor:.2f}")
print(f"inverción en bolsa = S/ {bolsa:.2f}")


