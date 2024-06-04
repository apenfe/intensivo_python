users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username, user_info in users.items():
    print(f'nombre de usuario: {username}')
    full_name = user_info['first'] + ' ' + user_info['last']
    print(f'full name: {full_name}')
    print(f"Localizacion: {user_info['location']}\n")