from pathlib import Path

libro = 'moby_dick.txt'
path = Path(libro)
texto = path.read_text(encoding='utf-8')
busqueda = 'the'
cuenta = texto.lower().count(busqueda)

print(f"{libro} tiene un total de {cuenta} palabras que coinciden con {busqueda}.")
