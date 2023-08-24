import os
os.system("cls")

def potencia(base,exponente):
    if(exponente==1) : return base
    return base * potencia(base,(exponente - 1))

print(potencia(9,2))

