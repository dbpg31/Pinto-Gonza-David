import os
os.system("cls")

numero_empleado = int(input("Ingrese el número asignado al empleado: "))


def obtener_estado_civil(numero):
    estado_civil = int(str(numero)[0])
    if estado_civil == 1:
        return "Soltero"
    elif estado_civil == 2:
        return "Casado"
    elif estado_civil == 3:
        return "Divorciado"
    elif estado_civil == 4:
        return "Viudo"
    else:
        return "Estado civil desconocido"

def obtener_edad(numero):
    edad = int(str(numero)[1:3])
    return edad

def obtener_genero(numero):
    genero = int(str(numero)[3])
    if genero == 1:
        return "Masculino"
    elif genero == 2:
        return "Femenino"
    else:
        return "Género desconocido"

estado_civil = obtener_estado_civil(numero_empleado)
edad = obtener_edad(numero_empleado)
genero = obtener_genero(numero_empleado)

print("Estado civil:", estado_civil)
print("Edad:", edad)
print("Género:", genero)
