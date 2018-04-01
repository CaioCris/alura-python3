# -*- coding: UTF-8 -*-

def imprime(nota_fiscal):
    print(f'Imprimindo nota fiscal {nota_fiscal.cnpj}')


def envia_email(nota_fiscal):
    print(f'Enviando nota fiscal por email {nota_fiscal.cnpj}')


def commit_bd(nota_fiscal):
    print(f'Commit no banco de dados da nota fiscal de cnpj:{nota_fiscal.cnpj}')