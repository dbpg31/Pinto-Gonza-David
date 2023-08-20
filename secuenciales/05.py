import os
os.system("cls")

gigabytes = int( input("gigabytes : "))

megabyte = gigabytes * 1024
kilobyte = megabyte * 1024
byte = kilobyte * 1024

print(f"megabyte = {format(megabyte,'.2f') } " )
print(f"kilobyte = {format(kilobyte,'.2f') } " )
print(f"byte = {format(byte,'.2f') } " )
