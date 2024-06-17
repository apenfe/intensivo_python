from pathlib import Path

nombre = input("Escriba su nombre: ")

path = Path("invitado.txt")

path.write_text(nombre)