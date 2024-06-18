from pathlib import Path
import json

path = Path('username.json')
contenido = path.read_text()
username = json.loads(contenido)

print(f"Bienvenido de nuevo {username}")