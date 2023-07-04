#Projeto de Python: entendendo a Orientação a Objetos.
#Leonardo Medeiros Silva Aparicio

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposito(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

