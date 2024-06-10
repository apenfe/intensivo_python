# Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def primera_mayuscula(string):

    j = 0
    salida = ""
    for i in string:
        if j == 0:
            salida += i.upper()
        else:
            salida += i
        j += 1

    return salida

print(primera_mayuscula("hola"))

