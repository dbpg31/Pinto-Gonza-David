import os
os.system("cls")

numero1= int(input("primer número : "))
numero2= int(input("segundo número : "))
numero3= int(input("tercer número : "))

if numero1 > numero2 and numero1 < numero3 : print("medio es : ",numero1)
elif numero1 < numero2 and numero1 > numero3 : print("medio es : ",numero1)
elif numero2 > numero1 and numero2 < numero3 : print("medio es : ",numero2)
elif numero2 < numero1 and numero2 > numero3 : print("medio es : ",numero2)

