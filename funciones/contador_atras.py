import os
os.system("cls")

# numero=int(input("Nùmero: "))

def cuenta_atras(numero):
    numero-=1
    if numero > 0 :
        print(numero)
        cuenta_atras(numero)
    

cuenta_atras(10)

