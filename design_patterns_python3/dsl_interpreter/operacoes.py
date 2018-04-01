class Soma:

    def __init__(self, esquerda, direita):
        self.__esquerda = esquerda
        self.__direita = direita

    def avalia(self):
        return self.__esquerda.avalia() + self.__direita.avalia()


class Subtracao:

    def __init__(self, esquerda, direita):
        self.__esquerda = esquerda
        self.__direita = direita

    def avalia(self):
        return self.__esquerda.avalia() - self.__direita.avalia()


class Numero:

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == '__main__':
    esquerda = Soma(Numero(10), Numero(20))
    direita = Soma(Numero(5), Numero(2))
    conta = Soma(esquerda, direita)
    print(conta.avalia())
