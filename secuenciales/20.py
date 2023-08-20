import os
os.system("cls")

dinero = int( input("monto de dinero = S/ "))

if dinero >= 200 :
    nbilletes=dinero // 200
    print(f"billetes de 200 = {nbilletes:.2f}")
    dinero = dinero % 200
if dinero >= 100 :
    nbilletes=dinero // 200
    print(f"billetes de 100 = {nbilletes:.2f}")
    dinero = dinero % 100
if dinero >= 50 :
    nbilletes=dinero // 50
    print(f"billetes de 50 = {nbilletes:.2f}")
    dinero = dinero % 50
if dinero >= 20 :
    nbilletes=dinero // 20
    print(f"billetes de 20 = {nbilletes:.2f}")
    dinero = dinero % 20
if dinero >= 10 :
    nbilletes=dinero // 10
    print(f"billetes de 10 = {nbilletes:.2f}")
    dinero = dinero % 10
if dinero >= 5 :
    nbilletes=dinero // 5
    print(f"moneda de 5 = {nbilletes:.2f}")
    dinero = dinero % 5
if dinero >= 2 :
    nbilletes=dinero // 2
    print(f"moneda de 2 = {nbilletes:.2f}")
    dinero = dinero % 2
if dinero >= 1 :
    nbilletes=dinero // 1
    print(f"moneda de 1 = {nbilletes:.2f}")
    dinero = dinero % 1

""" intento de lista
dinero = int( input("monto de dinero = S/ "))
lista = [200,100,50,20,10,5,2,1]
for N in lista:
    if dinero >= N:
        nbilletes=dinero // N
    print(f"cantidad de ('billete' if dinero >= 10 else 'moneda')= {N:.2f}")
    dinero = dinero % N"""