class Restaurante:

    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre_restaurante} y es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante está abierto")

class CarritoHelados(Restaurante):

    def __init__(self,nombre_restaurante="PEPE",tipo_cocina="ITALIANO",sabores="yogurt"):
        super().__init__(nombre_restaurante,tipo_cocina)
        self.sabores = sabores

    def consultar_sabor(self):
        print(f"El sabor es de: {self.sabores}")

helados = CarritoHelados()
helados.consultar_sabor()