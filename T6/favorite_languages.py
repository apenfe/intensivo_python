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

for nombre in favorite_languages.keys():
    print(f"A {nombre.title()} le encanta el lenguage de programacion...")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, gracias por venir a la piscina")

print("Los siguientes lenguages han sido tratados:")
for lenguage in favorite_languages.values():
    print(f"{lenguage.title()}")

print("Los siguientes lenguages han sido tratados:") # la funcion set, elimina valores duplicados, creando un conjunto
for lenguage in set(favorite_languages.values()):
    print(f"{lenguage.title()}")