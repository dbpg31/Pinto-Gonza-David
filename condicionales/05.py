import os
os.system("cls")

numero = int( input("nuemro de 4 cifras = "))

unidad = numero % 10
decena = int((numero % 100)/10)
centena = int((numero % 1000)/100)
millar = int((numero - (numero % 1000))/1000)

if  centena < decena and centena < unidad and centena < millar : menor = centena
elif decena < centena and decena < unidad and decena < millar : menor = decena
elif unidad < centena and unidad < decena and unidad < millar : menor = unidad
elif millar < centena and millar < decena and millar < unidad : menor = millar

if  centena > decena and centena > unidad and centena > millar : mayor = centena
elif decena > centena and decena > unidad and decena > millar : mayor = decena
elif unidad > centena and unidad > decena and unidad > millar : mayor = unidad
elif millar > centena and millar > decena and millar > unidad : mayor = millar


print("número mayor =",str(mayor) + str(menor))

