mensaje  = "Dime algo y lo repetire. \nEscribe quit para terminar: "

palabra = ""
while palabra != "quit":
    palabra = input(mensaje)

    if palabra != "quit":
        print(palabra)

print("Con bandera...")

check = True
while check:
    palabra = input(mensaje)

    if palabra != "quit":
        print(palabra)
    else:
        check = False