while True:

    edad = int(input("Cual es su edad?"))

    if edad >0 and edad <3:
        print("gratis")
    elif edad>=3 and edad <=12:
        print("8 euros")
    elif edad > 12 and edad <=100:
        print("12 euros")
    else:
        print("inserte una edad valida")