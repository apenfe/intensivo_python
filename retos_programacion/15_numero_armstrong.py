# Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

def armstrong(numero):

    digitos = str(numero)

    total = 0
    for digito in digitos:

        total += int(digito)**len(digitos)

    if total == numero:
        return True
    else:
        return False

print(armstrong(9474))