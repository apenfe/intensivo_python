from pathlib import Path

archivos = ['perros.txt','gatos.txt']

for archivo in archivos:
    try:
        path = Path(archivo)
    except FileNotFoundError:
        print(f"fichero {path} no encontrado")
    else:
        contenido = path.read_text()
        print(contenido)