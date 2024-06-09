# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calculo_area(poligono):

    poligono=poligono.lower()

    if poligono == 'triangulo':

        base = float(input('Ingrese el base: '))
        altura = float(input('Ingrese el altura: '))
        area = base * altura
        return area

    elif poligono == 'cuadrado':

        lado = float(input('Ingrese el lado: '))
        area = lado * lado
        return area

    elif poligono == 'rectangulo':

        lado_1 = float(input('Ingrese el lado 1: '))
        lado_2 = float(input('Ingrese el lado 2: '))
        area = lado_1 * lado_2
        return area

    else:
        return None

poligono = input('Ingrese el nombre del poligono: ')
area = calculo_area(poligono)

if area!= None:
    print(f'El area es {area}')
else:
    print('Poligono no valido')

