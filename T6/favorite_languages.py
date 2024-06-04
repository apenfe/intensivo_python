favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"El lenguage favorito de sarah es {language}")

for nombre, lenguage in favorite_languages.items():
    print(f"A {nombre.title()} le encanta el lenguage de programacion {lenguage.title()}")