import os
import csv
from APP_PRODUCTIVIDAD.Administrador import Administrador
from APP_PRODUCTIVIDAD.Tarea import Tarea


class App:

    def __init__(self):
        self._administrador = Administrador()
        self._abrir_base_datos()

    def _abrir_base_datos(self):

        if os.path.isfile('./tareas.csv'):
            self._agregar_tareas()
            self._administrador.mostrar()
        else:
            with open('./tareas.csv', 'w'):
                pass

        self._ejecutar()

    def _agregar_tareas(self):
        with open('./tareas.csv', 'r') as archivo:
            reader = csv.reader(archivo)

            lineas = []
            for fila in reader:
                lineas.append(fila)
                tarea = Tarea(fila[0], fila[1], fila[2])
                if fila[3] == 'Completada':
                    tarea.estado = 'Completada'
                self._administrador.agregar_tarea(tarea)

    def _ejecutar(self):
        '''Aplicativo para la interacción con el usuario vía teclado'''

        continuar = True  # While "infinito"

        while continuar:
            print('\n\nSeleccione una opción: ')
            print('  (1) Mostrar administrador de tareas')
            print('  (2) Agregar tarea')
            print('  (3) Actualizar tarea')
            print('  (4) Eliminar tarea')
            print('  (5) Ver detalle de una tarea')
            print('  (6) Salir')

            opcion = int(input('Opción: '))

            if opcion == 1:  # Mostrar administrador
                # Mostrar menú de opciones:
                print('\n   Indique las categorías a mostrar: (a) todas, (b) filtrar')
                opcion_cat = input('   Opción: ')

                if opcion_cat.lower() == 'a':
                    self._administrador.mostrar()
                else:
                    print('\n      Especifique la categoría a mostrar: ')
                    cat = input('      Categoría: ')
                    self._administrador.mostrar(categoria=cat)
            elif opcion == 2:  # Agregar tarea
                print('Información de la tarea a agregar: ')
                descripcion = input('Descripción: ')
                categoria = input('Categoría: ')
                detalles = input('Detalles: ')
                tarea = Tarea(descripcion, categoria, detalles)
                self._administrador.agregar_tarea(tarea)
                self._administrador.mostrar()
            elif opcion == 3:  # Actualizar tarea
                self._administrador.mostrar()
                print('\nID de la tarea a actualizar: ')
                ID = int(input('ID: '))
                self._administrador.actualizar_tarea(ID)
                self._administrador.mostrar()
            elif opcion == 4:  # Eliminar tarea
                self._administrador.mostrar()
                print('\nID de la tarea a eliminar: ')
                ID = int(input('ID: '))
                respuesta = input('¿Seguro que desea eliminar la tarea? (S/N): ')
                if respuesta.lower() == 's':
                    self._administrador.eliminar_tarea(ID)
                self._administrador.mostrar()
            elif opcion == 5:  # Ver detalle de una tarea
                self._administrador.mostrar()
                print('\nIntroduzca el ID de la tarea que quiere ver en detalle: ')
                ID = int(input('ID: '))
                self._administrador.detalle_tarea(ID)
            elif opcion == 6:  # Salir
                continuar = False
                self._actualizar_base_datos()
                break
            else:
                print('Debe seleccionar una opción entre 1 y 6')

            input('Oprima una tecla para continuar...')

            # *** ADICIONAL: LIMPIAR PANTALLA ***
            os.system('cls')  # En Windows
            # os.system('clear')  # En Mac

    def _actualizar_base_datos(self):
        '''Actualiza el archivo CSV con las tareas agregadas/modificadas durante la sesión'''
        with open('./tareas.csv', 'w') as archivo:
            writer = csv.writer(archivo)

            if len(self._administrador.tareas) != 0:  # si hay tareas
                for tarea in self._administrador.tareas:
                    fila = [tarea.descripcion, tarea.categoria, tarea.detalles, tarea.estado]
                    writer.writerow(fila)

if __name__ == "__main__":
    app = App()