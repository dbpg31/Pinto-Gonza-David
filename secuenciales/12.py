import os
os.system("cls")

import math

Ncudratica = int( input("coeficiente de la variable cuadratica = "))
Nlineal = int( input("coeficiente de la variable lineal = "))
Nindependiente = int( input("termino independiente = "))

respuesta1 = (-Nlineal + math.sqrt(Nlineal**2-(4*Ncudratica*Nindependiente)))/(2*Ncudratica)
respuesta2 = (-Nlineal - math.sqrt(Nlineal**2-(4*Ncudratica*Nindependiente)))/(2*Ncudratica)

print(f"respuesta 1 = {respuesta1:.2f}")
print(f"respuesta 2 = {respuesta2:.2f}")
