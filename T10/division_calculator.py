print("Dame dos numeros y los dividiré: ")
print("Inserte q para salir")

while True:
    primero = input("Inserte un numero: ")
    if primero == 'q':
        break
    segundo = input("Inserte un numero: ")
    if segundo == 'q':
        break

    try:
        respuesta = int(primero)/int(segundo)
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        print(respuesta)
