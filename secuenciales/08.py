import os
os.system("cls")

import math

radio = int( input("radio : "))
altura = int( input("altura : "))

areaBase = math.pi * math.pow(radio,2)
areaLateral = 2 * math.pi * radio * altura
areaTotal = 2 * areaBase * areaLateral

print(f"area de la base = {format(areaBase,'.2f') } " )
print(f"area lateral = {format(areaLateral,'.2f') } " )
print(f"area total = {format(areaTotal,'.2f') } " )