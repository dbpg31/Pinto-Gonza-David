import os
os.system("cls")

nota1 = int(input("1ra nota = "))
nota2 = int(input("2da nota = "))
nota3 = int(input("3ra nota = "))
nota4 = int(input("4ta nota = "))
nota5 = int(input("5ta nota = "))


if nota1 > nota5 and nota1 > nota4 and nota1 > nota3 and nota1 > nota2 : mayor = nota1
elif nota2 > nota5 and nota2 > nota4 and nota2 > nota3 and nota2 > nota1 : mayor = nota2
elif nota3 > nota5 and nota3 > nota4 and nota3 > nota2 and nota3 > nota1 : mayor = nota3
elif nota4 > nota5 and nota4 > nota3 and nota4 > nota2 and nota4 > nota1 : mayor = nota4
elif nota5 > nota4 and nota5 > nota3 and nota5 > nota2 and nota5 > nota1 : mayor = nota5

if nota1 < nota5 and nota1 < nota4 and nota1 < nota3 and nota1 < nota2 : menor = nota1
elif nota2 < nota5 and nota2 < nota4 and nota2 < nota3 and nota2 < nota1 : menor = nota2
elif nota3 < nota5 and nota3 < nota4 and nota3 < nota2 and nota3 < nota1 : menor = nota3
elif nota4 < nota5 and nota4 < nota3 and nota4 < nota2 and nota4 < nota1 : menor = nota4
elif nota5 < nota4 and nota5 < nota3 and nota5 < nota2 and nota5 < nota1 : menor = nota5

promedio = ((nota1 + nota2 + nota3 + nota4 + nota5) - (mayor + menor))/3  

print("notas eliminasdas =",mayor,"y",menor)
print (f"promedio = {promedio:.2f}")
