import os
os.system("cls")

numero = int(input("nuemro de 3 cifras : "))

unidad = numero % 10
decena = int((numero % 100)/10)
centena = int((numero % 1000)/100)

if unidad == decena - 1 and decena == centena - 1 : print(numero ,": es consecutivo descendente")
elif unidad == decena + 1 and decena == centena + 1 : print(numero,": es consecutivo ascendente")
else : print(numero,": no es consecutivo")
