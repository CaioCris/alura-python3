from datetime import date


class Pedido:

    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao


from abc import ABCMeta, abstractclassmethod


class Comando:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def executa(self):
        pass


class ConcluiPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


class PagaPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class FilaDeTrabalho:

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


if __name__ == '__main__':
    pedido01 = Pedido('Caio', 200)
    pedido02 = Pedido('Rafael', 100)
    pedido03 = Pedido('Lucas', 300)

    fila = FilaDeTrabalho()

    conclui = ConcluiPedido(pedido01)
    paga = PagaPedido(pedido01)

    fila.adiciona(conclui)
    fila.adiciona(paga)
