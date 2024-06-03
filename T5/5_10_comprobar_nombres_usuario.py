users = ['juan','luis','admin']
nuevos = ['joan','juan']
usuarios_minusculas = [user.lower() for user in users]

for nuevo in nuevos:

    if nuevo.lower() in usuarios_minusculas:
        print("cambie de nombre")
    else:
        print("Nombre correcto")

