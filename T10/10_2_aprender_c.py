from pathlib import Path

path = Path('aprender_python.txt')
contenido = path.read_text()

contenido = contenido.replace("python","C")
print(contenido)

lineas = contenido.splitlines()

for linea in lineas:
    print(linea)