import os
os.system("cls")

import math

radio = int( input("radio : ") )
altura = int( input("altura : ") )

areaTotal = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * math.pow(radio,2) * altura

print(f"area total = {format(areaTotal,'.2f') } " )
print(f"volumen = {format(volumen,'.2f') } " )
