from design_patterns_python3.chain_of_responsibility.descontos import DescontoPorQuantidade, DescontoPorValor, SemDesconto


class CalculadorDeDescontos:

    def calcula(self, orcamento):
        desconto = DescontoPorQuantidade(DescontoPorValor(SemDesconto())).calcula(orcamento)
        return desconto


if __name__ == '__main__':
    from design_patterns_python3.chain_of_responsibility.orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item -1', 100))
    orcamento.adiciona_item(Item('Item -2', 300))
    orcamento.adiciona_item(Item('Item -3', 800))
    orcamento.adiciona_item(Item('Item -4', 900))
    orcamento.adiciona_item(Item('Item -5', 50))
    orcamento.adiciona_item(Item('Item -6', 120))

    print(orcamento.valor)

    calculador = CalculadorDeDescontos()
    desconto_calculado = calculador.calcula(orcamento)
    print(f'Desconto calculado {desconto_calculado:.2f}')
