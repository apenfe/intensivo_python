from pathlib import Path

cadena = ""
nombre = ""
while nombre != quit:
    nombre = input("Inserte un nombre (quit para terminar): ")

    if nombre == 'quit':
        break
    else:
       cadena += nombre + "\n"

path = Path('libro_invitados.txt')
path.write_text(cadena)