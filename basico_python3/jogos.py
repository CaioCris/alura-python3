import forca

from basico_python3 import adivinhacao

print('********************************')
print('Escolha algum dos jogos')
print('********************************')

print('Opções de jogos:\n1- Forca\n2- Adivinhação')

jogo = int(input('Qual jogo vamos jogar ?'))

if jogo == 1:
    print('Jogo forca selecionado')
    forca.jogar_forca()
elif jogo == 2:
    print('Jogo adivinhação selecionado')
    adivinhacao.jogar_adivinhacao()

