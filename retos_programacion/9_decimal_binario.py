# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def decimal_binario(numero):
    salida = ""
    while numero > 0:

        if numero % 2 == 0:
            salida += "0"
        else:
            salida += "1"

        numero=numero//2

    return salida[::-1]

print(decimal_binario(11))

