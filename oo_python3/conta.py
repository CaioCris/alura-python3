class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        #print(f'Contruindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O Saldo de {self.saldo} do titular {self.titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __posso_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__posso_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite!')

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @staticmethod
    def codigo_banco():
        return '001'

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limites(self):
        return self.__limite

    @limites.setter
    def limites(self, limite):
        self.__limite = limite
