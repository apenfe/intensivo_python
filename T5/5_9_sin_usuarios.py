users = ['juan','luis','admin']

if users:

    for user in users:

        if user == 'admin':
            print("Bienvenido super usuario")
        else:
            print(f"Bienvenido {user}")
else:
    print("No hay usuarios")