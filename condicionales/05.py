import os
os.system("cls")

numero = int( input("nuemro de 4 cifras = "))

unidad = numero % 10
decena = int((numero % 100)/10)
centena = int((numero % 1000)/100)
millar = int((numero - (numero % 1000))/1000)

menor = millar
if  centena < menor : menor = centena
elif decena < menor : menor = decena
elif unidad < menor : menor = unidad

mayor = millar 
if centena > mayor : mayor = centena 
elif decena > mayor : mayor = decena
elif unidad > mayor : mayor = unidad 

mayorCen = centena
if centena >= decena : mayorCen = decena

numeromaximo = (mayor * 1000) + (mayorCen * 100) + (decena * 10) + menor

print(f"número max : {numeromaximo}")









# if cifra1 > cifra2 and cifra1 > cifra3 and cifra1 > cifra4 : n1 = cifra1
# elif cifra2 > cifra1 and cifra2 > cifra3 and cifra2 > cifra4 : n1 = cifra2
# elif cifra3 > cifra1 and cifra3 > cifra2 and cifra3 > cifra4 : n1 = cifra3
# elif cifra4 > cifra1 and cifra4 > cifra2 and cifra4 > cifra3 : n1 = cifra4
# n4 = 0
# elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra1
# elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra2
# elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra3
# elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra4

print(str(n1),str(n4))


#elif cifra2 > cifra1 and cifra2 > cifra3 and cifra2 > cifra4 : n4 = cifra2




"""cifra4 = numero % 10
cifra3 = int((numero % 100)/10)
cifra2 = int((numero % 1000)/100)
cifra1 = int((numero - (numero % 1000))/1000)

print("suma de cifras =",(cifra1 + cifra2 + cifra3 + cifra4))"""

