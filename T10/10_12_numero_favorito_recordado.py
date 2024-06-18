from pathlib import Path
import json

path = Path('otro_numero_favorito.json')

if path.exists():
    content = path.read_text()
    num = json.loads(content)
    print(f"Numero favorito: {num}")
else:
    num = int(input("Inserte su numero favorito: "))
    path = Path('otro_numero_favorito.json')
    contents = json.dumps(num)
    path.write_text(contents)