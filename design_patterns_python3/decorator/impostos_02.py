from abc import ABCMeta, abstractmethod


def Imposto(calcula):
    def wrapper(self, orcamento):
        return calcula(self, orcamento) + 50
    return wrapper


class TemplateImposto(metaclass=ABCMeta):

    @Imposto
    def calcula(self, orcamento):
        if self.deve_taixar(orcamento):
            return self.maxima_taixa(orcamento)
        else:
            return self.minima_taixa(orcamento)

    @abstractmethod
    def deve_taixar(self, orcamento):
        pass

    @abstractmethod
    def maxima_taixa(self, orcamento):
        pass

    @abstractmethod
    def minima_taixa(self, orcamento):
        pass


class ISS:

    @Imposto
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS:

    @Imposto
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


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
