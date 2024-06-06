# empieza con usuarios que hay que verificar,
# y una lista vacia para alojar a los usuarios confirmados.

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# verifica cada usuario hasta que ya no hay usuarios sin confirmar.
# Mueve a cada usuario verificado a la lista de usuarios confirmados.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verificando usuario: {current_user.title()}")
    confirmed_users.append(current_user)

# Muestra todos los usuarios confirmados.
print(f"\nLos siguientes usuarios estan confirmados: ")
for confirmed in confirmed_users:
    print(confirmed.title())