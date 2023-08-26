import os
os.system("cls")

notaMatematicas = int(input("Ingrese la nota de Matemáticas: "))
notaFisica = int(input("Ingrese la nota de Física: "))

propinaMatematicas = 3 if notaMatematicas > 17 else 1
propinaFisica = 2 if notaFisica > 15 else 0.50

promedio = (notaMatematicas + notaFisica) / 2

if promedio > 16:
    obsequio = "reloj"
else:
    obsequio = "ninguno"

print("Propina por Matemáticas: S/.", propinaMatematicas)
print("Propina por Física: S/.", propinaFisica)
print("Promedio de notas: ", promedio)
print("Obsequio: ", obsequio)