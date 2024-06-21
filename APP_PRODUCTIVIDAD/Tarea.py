import textwrap

class Tarea:
    
    def __init__(self, descripcion, categoria, detalles):
        self._descripcion = descripcion
        self._categoria = categoria
        self._detalles = detalles
        self._estado = 'Pendiente'
        
    @property
    def descripcion(self):
        return self._descripcion

    @property
    def categoria(self):
        return self._categoria

    @property
    def detalles(self):
        return self._detalles

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        self._estado=nuevo_estado

    def mostrar(self):

        ancho = 80
        str_detalles = f'Detalles: {self._detalles}'

        if len(str_detalles) > ancho:
            detalles = textwrap.fill(str_detalles, width=ancho)
        else:
            detalles = str_detalles
            
        print('='*ancho)
        print(f'Tarea: {self._descripcion}')
        print('=' * ancho)
        print(f'Categoria: {self._categoria}')
        print('.' * ancho)
        print(f'Estado: {self._estado}')
        print('.' * ancho)
        print(detalles)
        print('=' * ancho)