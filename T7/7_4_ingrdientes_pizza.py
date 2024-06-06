frase = "\nInserta el ingrediente a su pizza:"
frase += "\n(Escribe quit cuando quieras terminar) "

while True:
    ingrediente = input(frase)

    if ingrediente == 'quit':
        break
    else:
        print(f"Añadiendo {ingrediente.title()} a la pizza")