class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f'Contruindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O Saldo de {self.saldo} do titular {self.titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limites(self):
        return self.__limite

    def set_limites(self, limite):
        self.__limite = limite
