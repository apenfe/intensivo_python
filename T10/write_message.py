from pathlib import Path

path = Path('programming.txt')
contenido = "me encanta programar\n"
contenido += "Me encanta crear nuevos juegos\n"
contenido += "Y tambein me encanta trabajar con datos\n"

path.write_text(contenido)