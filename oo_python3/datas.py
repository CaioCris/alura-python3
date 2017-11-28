class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formata(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

