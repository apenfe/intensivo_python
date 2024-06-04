numeros_favoritos = {
    'luis':[23,14],
    'adrian':[1,5,7],
    'maria':[22]
}

for nombre, numeros in numeros_favoritos.items():
    print(f"{nombre}: ")
    for numero in numeros:
        print(f"{numero}")