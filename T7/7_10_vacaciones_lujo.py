respuestas = {}

# configura una bandera para indicar que el polling esta activo
polling_active = True

while polling_active:

    name = input("\n Cual es tu nombre?")
    response = input("A donde te gustaria viajar? ")

    respuestas[name] = response

    repeat = input("te gustaria añadir a otra persona? (yes/no)")
    if repeat == 'no':
        polling_active=False

print("\n poll request-----")
for name, response in respuestas.items():
    print(f"name: {name}, respuesta: {response}.")
    