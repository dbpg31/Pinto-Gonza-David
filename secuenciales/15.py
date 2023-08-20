import os
os.system("cls")

juan = int( input("aporte de juan = $ "))
rosa = int( input("aporte de Rosa = $ "))
daniel = int( input("aporte de Daniel = S/ "))

invercion = juan + rosa + (daniel / 3)

Pjuan = (juan / invercion) * 100
Prosa = (rosa / invercion) * 100
Pdaniel = ((daniel / 3) / invercion) * 100

print(f"invercion total = $ {invercion:.2f}")
print(f"porcentaje de Juan = {Pjuan:.2f}%")
print(f"porcentaje de Rosa = {Prosa:.2f}%")
print(f"porcentaje de Daniel = {Pdaniel:.2f}%")

