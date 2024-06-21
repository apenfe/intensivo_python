class Administrador:

    def __init__(self):
        self._tareas = []

    @property
    def tareas(self):
        return self._tareas

    def mostrar(self,categoria=None):

        if len(self._tareas) != 0:
            ancho_col = 80

            formato_cols = '{0:<6} {1:<35} {2:<25} {3:<11}'
            print('='*ancho_col)
            print(formato_cols.format('ID','Tarea','Categoria','Estado'))
            print('='*ancho_col)

            if categoria == None:
                for ID, tarea in enumerate(self._tareas): # enumerate produce un indice y un elemento
                    print(formato_cols.format(str(ID + 1), tarea.descripcion, tarea.categoria, tarea.estado))
                    print('.' * ancho_col)
            else:
                for ID, tarea in enumerate(self._tareas):
                    if tarea.categoria == categoria:
                        print(formato_cols.format(str(ID + 1), tarea.descripcion, tarea.categoria, tarea.estado))
                        print('.' * ancho_col)
        else:
            print('*** NO HAY TAREAS DISPONIBLES ***')

    def agregar_tarea(self, tarea):
        '''Agregar una tarea al listado'''
        self._tareas.append(tarea)