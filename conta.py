# o self é responsavel por vincular os atributos com os argumentos que são enviados para uma função ou método
class Conta:
    def __init__(self, numero, titular, saldo, limite): #init define o construtor da classe, onde serão definidos os atributos
        print("Construindo objeto... {}".format(self))
        self.__numero = numero  #"__" antes do atributo é a mesma coisa que o private em java
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #é possível criar um método privado também
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, destino):
        self.saque(valor) #self pode servir pra chamar um método também
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property #simplifica o chamado do método get - conte.limite
    def limite(self):
        return self.__limite


    @limite.setter #simplifica o chamado do método setter - conta.limite = (valor desejado)
    def limite(self, limite):
        self.__limite = limite
