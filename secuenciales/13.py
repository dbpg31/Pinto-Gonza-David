import os
os.system("cls")

import math

cateto1 = int( input("cateto 1 = "))
cateto2 = int( input("cateto 2 = "))

hipotenusa = math.sqrt(math.pow(cateto1,2) + math.pow(cateto2,2))

print(f"hipotenusa = {hipotenusa:.2f}")

