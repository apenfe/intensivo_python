from T8.formatted_name import get_formatted_name
def greet_user(name):
    print(f"Hola, {name}")

greet_user("adrian")

while True:
    print("\nInserte su nombre, pulse q para salir. ")
    f_name = input("nombre: ")
    l_name = input("apellido: ")

    if f_name == "q" or l_name == "q":
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(formatted_name)