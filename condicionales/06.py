import os
os.system("cls")

edad1 = int( input("edad 1 : "))
edad2 = int( input("edad 2 : "))
edad3 = int( input("edad 3 : "))

if edad1 > edad3 and edad1 > edad2 : print("edad mayor =",edad1)
elif edad2 > edad1 and edad2 > edad3 : print("edad mayor =",edad2)
elif edad3 > edad1 and edad3 > edad2 : print("edad mayor =",edad3)

if edad1 < edad3 and edad1 < edad2 : print("edad menor =",edad1)
elif edad2 < edad1 and edad2 < edad3 : print("edad menor =",edad2)
elif edad3 < edad1 and edad3 < edad2 : print("edad menor =",edad3)

