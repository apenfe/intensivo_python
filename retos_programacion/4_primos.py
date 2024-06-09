# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def primos(n=100):

    primos = []

    for i in range(2,n+1):

        for j in range(2,i+1):

            if i % j == 0:

                if(primos):

                    for primo in primos:

                        if i % primo == 0:
                            print(i)
                            primos.append(i)
                else:
                    print(i)
                    primos.append(i)

    return primos

def primos_2(n=100):

    primos = [2]

    for i in range(2,n+1):

        primo = False

        for j in primos:

            if i % j == 0:
                primo = False
                break
            else:
                primo = True

        if primo:
            primos.append(i)

    return primos

print(primos_2())