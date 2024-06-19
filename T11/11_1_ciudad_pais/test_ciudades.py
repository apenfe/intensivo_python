from ciudad_funciones import *

def test_ciudad_pais():
    texto = formato('santiago', 'chile')
    assert texto == 'La ciudad de Santiago es la capital de Chile'

def test_ciudad_pais_habitantes():
    texto = formato('santiago', 'chile',500000)
    assert texto == 'La ciudad de Santiago es la capital de Chile, tiene 500000 habitantes.'
