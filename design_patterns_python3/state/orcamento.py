from abc import ABCMeta, abstractmethod


class EstadoOrcamento:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.desconto_aplicado =False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não pode ir para finalizado')


class Aprovado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')

    def aprova(self, orcamento):
        raise Exception('Orçamento já está aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento aprovado não pode ser reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovados não pode ser aprovados')

    def reprova(self, orcamento):
        raise Exception('Orçamento reprovados não pode ser reprovados novamente')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser aprovados')

    def reprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser reprovado')

    def finaliza(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser finalizado novamente')


class Orcamento:

    def __init__(self):
        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor

        return total

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)


class Item:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('01', 100))
    orcamento.adiciona_item(Item('02', 200))
    orcamento.adiciona_item(Item('03', 300))

    print(orcamento.valor)
    orcamento.aprova()
    orcamento.finaliza()
