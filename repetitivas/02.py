import os
os.system("cls")

multiplicando = int(input("multiplicando = "))
multiplicador = int(input("multiplicador = "))

producto = 0

while multiplicador > 0 :
    producto += multiplicando
    multiplicador -= 1
print(f"producto = {producto}")