from pathlib import Path
import json

numero = int(input("Digite su numero favorito: "))

path = Path('numero_favorito.json')
contenido = json.dumps(numero)
path.write_text(contenido)