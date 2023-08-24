import os
os.system("cls")

num1 = int(input("multiplicador : "))
num2 = int(input("multiplicando : "))

producto = 0

while num2 > 0 :
    producto += num1
    num2 -=1

print(f"producto : {producto}")


