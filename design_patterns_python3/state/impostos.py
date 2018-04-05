from abc import ABCMeta, abstractmethod


class Imposto(metaclass=ABCMeta):

    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    @abstractmethod
    def calcula(self, orcamento):
        pass

    def calculo_outro_imposto(self, orcamento):
        if self.__outro_imposto is not None:
            return self.__outro_imposto.calcula(orcamento)
        else:
            return 0


class TemplateImposto(Imposto, metaclass=ABCMeta):

    def calcula(self, orcamento):
        if self.deve_taixar(orcamento):
            return self.maxima_taixa(orcamento) + self.calculo_outro_imposto(orcamento)
        else:
            return self.minima_taixa(orcamento) + self.calculo_outro_imposto(orcamento)

    @abstractmethod
    def deve_taixar(self, orcamento):
        pass

    @abstractmethod
    def maxima_taixa(self, orcamento):
        pass

    @abstractmethod
    def minima_taixa(self, orcamento):
        pass


class ISS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_outro_imposto(orcamento)


class ICMS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_outro_imposto(orcamento)


class ICPP(TemplateImposto):

    def deve_taixar(self, orcamento):
        return orcamento.valor > 500

    def maxima_taixa(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taixa(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateImposto):

    def deve_taixar(self, orcamento):
        return orcamento.valor > 500 and self.__item_maior_100(orcamento)

    def maxima_taixa(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taixa(self, orcamento):
        return orcamento.valor * 0.06

    def __item_maior_100(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
