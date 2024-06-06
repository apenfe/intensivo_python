number = input("Dime un numero y te dire si es par o impar: ")
number = int(number)

if(number % 2 == 0):
    print(number, "es par")
else:
    print(number, "es impar")