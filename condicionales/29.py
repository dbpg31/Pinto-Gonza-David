

horastrabajadas = float(input("Ingrese las horas trabajadas: "))
pago = float(input("Ingrese el pago por hora: "))

if horastrabajadas <= 48:
    sueldobruto = horastrabajadas * pago
else:
    horasnormales = 48
    horasextra = horastrabajadas - horasnormales
    sueldobruto = (horasnormales * pago) + (horasextra * pago * 1.2)

if sueldobruto > 1500:
    descuento = sueldobruto * 0.11
else:
    descuento = 0

totalpago = sueldobruto - descuento

print("Horas trabajadas: ", horastrabajadas)
print("Pago por hora: S/.", pago)
print("Sueldo bruto: S/.", sueldobruto)
print("Descuento: S/.", descuento)
print("Total a pagar: S/.", totalpago)
