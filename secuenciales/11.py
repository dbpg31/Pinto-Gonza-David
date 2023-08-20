import os
os.system("cls")

numero1 = int( input("ingresar 1er numero : "))
numero2 = int (input("ingresar 2do numero : "))

n1cifra3 = numero1 % 10
n1cifra2 =int((numero1 % 100)/10)
n1cifra1 =int((numero1 - (numero1 % 100))/100)

n2cifra3 = numero2 % 10
n2cifra2 = int((numero2 % 100)/10)
n2cifra1 = int((numero2 - (numero2 % 100))/100)

print("nuevo primer numero = ",str(n2cifra3) + str(n1cifra2) + str(n2cifra1))
print("nuevo segundo numero = ",str(n1cifra3) + str(n2cifra2) +str(n1cifra1))