import os
os.system("cls")

def multiplicar(multiplicando,multiplicador):
    if(multiplicador==1) : return multiplicando
    return multiplicando + multiplicar(multiplicando,(multiplicador - 1))

print(multiplicar(9,9)) 




