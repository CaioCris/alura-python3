from design_patterns_python3.decorator.impostos import ISS, ICMS, ICPP, IKCV


class CalculadorDeImpostos:

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        return f'{imposto_calculado:.2f}'


if __name__ == '__main__':
    from design_patterns_python3.decorator.orcamento import Orcamento, Item

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item -1', 500))
    orcamento.adiciona_item(Item('Item -2', 50))
    orcamento.adiciona_item(Item('Item -3', 100))
    orcamento.adiciona_item(Item('Item -4', 350))
    orcamento.adiciona_item(Item('Item -5', 1000))
    orcamento.adiciona_item(Item('Item -6', 780))

    print(calculador.realiza_calculo(orcamento, ISS()))
    print(calculador.realiza_calculo(orcamento, ICMS()))
    print(calculador.realiza_calculo(orcamento, ICPP()))
    print(calculador.realiza_calculo(orcamento, IKCV()))
