from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    content = path.read_text()
    username = json.loads(content)
    print(f"Bienvenido, {username}")
else:
    username = input("Enter your name: ")
    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"Te recordare cuando vuelvas a acceder {username}")