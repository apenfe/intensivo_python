lugares_favoritos = {
    'jen': ['paris', 'madrid'],
    'sarah': ['pekin', 'tokio'],
    'edward': ['tallin'],
    'phil': ['odessa', 'kiev'],
}

for nombre, lugares in lugares_favoritos.items():
    print(f'{nombre}:')
    for lugare in lugares:
        print(f'\t{lugare}')