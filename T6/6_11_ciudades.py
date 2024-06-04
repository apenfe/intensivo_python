ciudades = {
    'paris':{
        'pais':'francia',
        'idioma':'frances',
    },
    'madrid':{
        'pais':'espagna',
        'idioma':'espagnol',
    }
}

for ciudad, info_ciudad in ciudades.items():
    print(f'nombre de ciudad: {ciudad}')
    print(f'Pais: {info_ciudad['pais']}')
    print(f'Idioma: {info_ciudad['idioma']}\n')