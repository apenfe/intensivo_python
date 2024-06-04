favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'adrian': None,
    'phil': 'python',
}

for nombre, lenguage in favorite_languages.items():

    if lenguage != None:
        print(f"A {nombre.title()} le encanta el lenguage de programacion {lenguage.title()}")
    else:
        print(f"{nombre.title()} aun debe de realizar la encuesta")