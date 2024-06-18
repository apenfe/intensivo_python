def sumar():
    uno = input('Inserte el primer numero:')
    dos = input('Inserte el segundo numero:')

    suma = 0
    try:
        suma = int(uno) + int(dos)
    except Exception as e:
        print("inserte dos numeros")
    else:
        print(suma)

while True:

    sumar()
    respuesta = input("Desea seguir sumando numeros? (N)")

    if respuesta == "N" or respuesta == 'n':
        break