import os
os.system("cls")

pies = int(input("pies : "))
pulgadas = int( input("puldas : "))

metros = (pies * 1/3.2808) + (pulgadas * 0.0254)

print(f"metros = {format (metros,'.2f')}")
