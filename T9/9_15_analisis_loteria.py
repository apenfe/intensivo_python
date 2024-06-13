import random

numeros = list(range(1, 11))
letras = ['A', 'B', 'C', 'D', 'E']
lista = numeros + letras

mi_boleto = [1,2,3,4,5,6,7,8,9,10,"A","D","C"]

intentos = 0

while True:
    intentos += 1
    count = 0
    elementos_premiados = random.sample(lista, 6)

    for premiado in elementos_premiados:

        if premiado in mi_boleto:
            count += 1

    if count == 4:
        mensaje = f"¡Felicitaciones! Suboleto esta premiado: {intentos}"
        break
    else:
        print(intentos)

print(mensaje)
