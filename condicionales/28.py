import os
os.system("cls")

hora_24h = input("Ingrese la hora en formato de 24 horas (HH:MM): ")

try:
    hora_minutos = hora_24h.split(":")
    hora = int(hora_minutos[0])
    minutos = int(hora_minutos[1])

    if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
        raise ValueError("Hora inválida")

    if hora < 12:
        periodo = "AM"
        if hora == 0:
            hora = 12
    else:
        periodo = "PM"
        if hora > 12:
            hora -= 12

    hora_12h = "{:02d}:{:02d} {}".format(hora, minutos, periodo)
    print("Hora en formato de 12 horas: ", hora_12h)

except ValueError as e:
    print("Error:", e)