import os
os.system("cls")

numero = int( input("numero de 4 cifras : "))

cifra4 = numero % 10
cifra3 = int((numero % 100)/10)
cifra2 = int((numero % 1000)/100)
cifra1 = int((numero - (numero % 1000))/1000)

print("suma de cifras =",(cifra1 + cifra2 + cifra3 + cifra4))




