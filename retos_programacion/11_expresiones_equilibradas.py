# Crea un programa que comprueba si los paréntesis, llaves y corchetes
# de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# - Expresión no balanceada: { a * ( c + d ) ] - 5 }

def balanceda(expresion):

    parentesis = 0
    corchetes = 0
    llaves = 0

    for letra in expresion:

        if letra == '{':
            llaves += 1
        elif letra == '}':
            llaves -= 1
        elif letra == '(':
            parentesis += 1
        elif letra == ')':
            parentesis -= 1
        elif letra == '[':
            corchetes += 1
        elif letra == ']':
            corchetes -= 1

    if (parentesis+corchetes+llaves) == 0:
        return True
    else:
        return False

print(balanceda('{ [ a * ( c + d ) ] - 5 }'))
print(balanceda(' { a * ( c + d ) ] - 5 }'))
