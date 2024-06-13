from random import randint


class Dados:

    def __init__(self,caras = 6):
        self.caras = caras

    def tirar_dados(self):
        print(randint(1,self.caras))

dado_6 = Dados(6)
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()
dado_6.tirar_dados()

dado_10 = Dados(10)
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()
dado_10.tirar_dados()