
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero  #__ é a mesma coisa que o private em java
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saque(valor) #self pode servir pra chamar um método também
        destino.deposito(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get__limite(self):
        return self.__limite

    def set__limite(self, limite):
        self.__limite = limite
