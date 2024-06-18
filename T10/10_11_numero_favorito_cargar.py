from pathlib import Path
import json

path = Path('numero_favorito.json')
content = path.read_text()
numero = json.loads(content)
print(f"Su numero favorito es el: {numero}")
