import os
os.system ("cls")

kilometros = int( input("kilometros : "))
pies = int (input("pies : "))
millas = int (input("millas : "))

metros = (kilometros * 1000) + (pies * 1/3.2808) + (millas * 1609)
yardas = metros * 1.0936

print(f" metros = {format(metros,'.2f') } " )
print(f"yardas = {format (yardas,'.2f') } " )





