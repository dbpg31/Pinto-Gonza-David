import os
os.system("cls")

nota1 = int( input("practica 1 : "))
nota2 = int( input("practica 2 : "))
nota3 = int( input("practica 3 : "))

if nota3 >= 10 : nota3 = nota3 + 2

notaFinal = (nota1 + nota2 + nota3)/3

print(f"promedio final = {notaFinal:.2f}")
