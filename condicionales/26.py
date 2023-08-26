import os
os.system("cls")

monto= int(input("Ingrese el monto total de la compra: "))

if monto > 5000:
    prestamo = monto * 0.30
else:
    prestamo = monto * 0.20

interes = prestamo * 0.10
pagoEmpresa = monto - prestamo + interes

print("Monto a pagar con préstamo: $", prestamo)
print("Monto a pagar de su propio dinero: $", pagoEmpresa)
