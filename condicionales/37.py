










mensaje = ""
if Pamela > mitad : mensaje = "Ganó Pamela"
elif Pamela > mitad : mensaje = "Ganó Karol"
elif Pamela > mitad : mensaje = "Ganó Fany"
elif Pamela < Karol and Pamela < Fany : mensaje = "Pasan a 2da vuelta : Karol y Fany"
elif Karol < Pamela and Karol < Fany : mensaje = "Pasan a 2da vuelta : Pamela y Fany"
elif Fany < Karol and Fany < Pamela : mensaje = "Pasan a 2da vuelta : Pamela y Karol"
elif Pamela == Karol and Pamela == Fany and Karol == Fany : mensaje = "Elecciones anuladas"
elif Pamela > Karol and Pamela > Fany and Karol == Fany : mensaje = "Elecciones anuladas"
elif Karol > Pamela and Karol > Fany and Pamela == Fany : mensaje = "Elecciones anuladas"
elif Fany > Pamela and Fany > Karol and Pamela == Karol : mensaje = "Elecciones anuladas"

lista = {"Pamela : ": Pamela, "Karol : ": Karol, "Fany : ":Fany }
orden = sorted(lista.items(),key=operator.itemgetter(1), reverse=True)

print(mensaje)
print(f"1er Lugar : { orden[0]}")
print(f"2do Lugar : { orden[1]}")
print(f"3er Lugar : { orden[2]}")
