import os
os.system("cls")

metros = int (input("metros : "))

centimetros = metros * 100
pulgadas = centimetros * 2.54
pies = pulgadas * 12
yardas = pies * 3

print( f" cemtimetros = {format (centimetros,'.2f') }")
print( f"pulgadas = {format(pulgadas,'.2f')}")
print( f"pies = {format(pies,'.2f')}")
print( f"yardas = {format(yardas,'.2f')}")