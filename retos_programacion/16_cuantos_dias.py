# Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

import re

def fecha_correcta(dia,mes,anio):

    # Comprobar la validez de los días en cada mes
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        # Comprobar año bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False

    return True

def dias(fecha1,fecha2):

    patron = r'^([1-9]|0[1-9]|[12][0-9]|3[01])/([1-9]|0[1-9]|1[0-2])/([0-9]{4})$'

    match1, match2 = re.match(patron, fecha1), re.match(patron, fecha2)

    if not match1 or not match2:
        return None

    dia, mes, anio = map(int, match1.groups())
    dia2, mes2, anio2 = map(int, match2.groups())

    # Si el patrón es correcto, verificar si la fecha es válida
    if fecha_correcta(dia,mes,anio) and fecha_correcta(dia2,mes2,anio2):
        return 1
    else:
        return None

print(dias("11/05/1995","13/05/1995"))