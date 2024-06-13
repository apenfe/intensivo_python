import random

numeros = list(range(1, 11))
letras = ['A', 'B', 'C', 'D', 'E']
lista = numeros + letras

elementos_premiados = random.sample(lista, 4)

mensaje = "¡Felicitaciones! Cualquier boleto con los siguientes números o letras está premiado: "
mensaje += ", ".join(map(str, elementos_premiados))

print(mensaje)