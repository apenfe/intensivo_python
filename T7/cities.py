frase = "\nInserta el nombre de una ciudad que has visitado:"
frase += "\n(Escribe quit cuando quieras terminar) "

while True:
    city = input(frase)

    if city == 'quit':
        break
    else:
        print(f"Me gustaria ir a {city.title()}")