favorite_languages = {
    'jen': ['Python', 'JavaScript'],
    'sarah': ['C++', 'JavaScript'],
    'edward': ['Ruby'],
    'phil': ['Python', 'Rust'],
}

for name, languages in favorite_languages.items():

    if(len(languages)>1):
        print(f"Los lenguages favoritos de {name.title()} son: ")
    else:
        print(f"El lenguage favorito de {name.title()} es: ")

    for language in languages:
        print(f"\t{language}")