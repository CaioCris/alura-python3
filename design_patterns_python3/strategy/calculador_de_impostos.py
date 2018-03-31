from design_patterns_python3.strategy.impostos import ISS, ICMS


class CalculadorDeImpostos:

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto(orcamento)
        return imposto_calculado


if __name__ == '__main__':
    from design_patterns_python3.chain_of_responsibility.orcamento import Orcamento

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)
    print(calculador.realiza_calculo(orcamento, ISS().calcula))
    print(calculador.realiza_calculo(orcamento, ICMS().calcula))
