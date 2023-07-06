#página criada para entendimento de get e setter

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property #teste para chamar a função nome apenas com cliente.nome
    def nome(self): #continua sendo um get mas sem o nome
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome