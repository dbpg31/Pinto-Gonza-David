import os
os.system("cls")

sexo = input("sexo : ")
edad = int (input("edad : "))

if sexo == "femenino" and edad <=23 : categoria = "FA"
elif sexo == "femenino" and edad > 23 : categoria = "FB"

if sexo == "masculino" and edad <=23 : categoria = "MA"
elif sexo == "masculino" and edad > 23 : categoria = "MB"

print(F"categoria del postulate : {categoria}")
