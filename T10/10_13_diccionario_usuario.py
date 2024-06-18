from pathlib import Path
import json

path = Path('usuario.json')

username = input("Enter your name: ")
age = int(input('Inserte su edad'))

usuario = {}

usuario["name"]=username
usuario["edad"]=age

contents = json.dumps(usuario)
path.write_text(contents)
print(f"Te recordare cuando vuelvas a acceder {usuario["name"]}")