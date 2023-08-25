import os
os.system("cls")

examen1 = int(input("nota 1 = ")) 
examen2 = int(input("nota 2 = "))
examen3 = int(input("nota 3 = "))

if examen1 >= 13 : aumento1 = 5
else : aumento1 = 0 
if examen2 >= 13 : aumento2 =  5
else : aumento2 = 0
if examen3 >= 13 : aumento3 = 5
else : aumento3 = 0

total = 20 + aumento1 + aumento2 + aumento3

print(f"total de propina = S/{total:.2f}")