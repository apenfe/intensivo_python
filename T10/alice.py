from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Lo siento, el fichero {path} no existe.")
else:
    words = contents.split()
    numero_palabras = len(words)
    print(f"{numero_palabras} palabras")