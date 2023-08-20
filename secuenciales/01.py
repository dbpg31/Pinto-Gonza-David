import os
os.system("cls")

varones = int( input("varones :") )
mujeres = int(input("mujeres : ") )
total = varones + mujeres

Pvarones = varones / total * 100
Pmujeres = mujeres / total * 100

print( f"% varones = {format ( Pvarones ,'.2f') }%")
print( f"% mujeres = {format (Pmujeres,'.2f') }%" ) 