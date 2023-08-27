


def convertirMayusculas(texto):
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()

Texto = input("Ingrese un texto: ")

Mayusculas = convertirMayusculas(Texto)
Minusculas = convertirMinusculas(Texto)

print("Texto en mayúsculas:", Mayusculas)
print("Textoen minúsculas:", Minusculas)
