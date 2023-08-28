import os
os.system("cls")

dividendo = int(input("Ingrese el dividendo = "))
divisor = int(input("Ingrese el divisor = "))

cociente = 0

while dividendo >= divisor:
    dividendo -= divisor 
    cociente += 1

resto = dividendo

print("Cociente:", cociente)
print("Resto:", resto)


