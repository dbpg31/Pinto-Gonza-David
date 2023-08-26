import os
os.system("cls")

a = int(input("nuemro a : "))
b = int(input("nuemro b : "))
c = int(input("nuemro c : "))

if a > b and b > c : print("esta en orden descendente")
elif a < b and b < c  : print("esta en orden ascendente")
else : print("esta desordenado")


