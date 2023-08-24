import os
os.system("cls")


def divisores(numero,divisor):
    if numero % divisor == 0 : print(divisor)
    if divisor < 1 : divisores(numero,divisor-1)

divisores(6,6)

