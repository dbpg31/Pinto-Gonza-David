impot os
os.system("cls")

numero = int( input("nuemro de 4 cifras = "))

cifra1 = int((numero - (numero % 1000))/1000)
cifra2 = int((numero % 1000)/100)
cifra3 = int((numero % 100)/10)
cifra4 = numero % 10

if cifra1 > cifra2 and cifra1 > cifra3 and cifra1 > cifra4 : n1 = cifra1
elif cifra2 > cifra1 and cifra2 > cifra3 and cifra2 > cifra4 : n1 = cifra2
elif cifra3 > cifra1 and cifra3 > cifra2 and cifra3 > cifra4 : n1 = cifra3
elif cifra4 > cifra1 and cifra4 > cifra2 and cifra4 > cifra3 : n1 = cifra4
n4 = 0
elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra1
elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra2
elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra3
elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4 : n4 = cifra4

print(str(n1),str(n4))


#elif cifra2 > cifra1 and cifra2 > cifra3 and cifra2 > cifra4 : n4 = cifra2




"""cifra4 = numero % 10
cifra3 = int((numero % 100)/10)
cifra2 = int((numero % 1000)/100)
cifra1 = int((numero - (numero % 1000))/1000)

print("suma de cifras =",(cifra1 + cifra2 + cifra3 + cifra4))"""

