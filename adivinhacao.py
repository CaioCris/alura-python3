import random

print('********************************')
print('Bem vindo ao jogo de Adivinhação')
print('********************************')

numero_secreto = round(random.randrange(1,101)) #Numeros entre 1 e 100
rodada = 1
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas + 1):
    print('Você esta na rodada {} de {} tentatias'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um numero entre 1 e 100: '))

    if chute < 1 or chute > 100:
        print('Seu numero deve ser entre 1 ou 100!')
        continue

    print('Você digitou', chute)

    #Variaveis com as condiçõs
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Errou! Você chutou muito alto!')
        elif menor:
            print ('Errou! Você chutou muito baixo')

    rodada = rodada + 1

    print('Fim do jogo')

print(numero_secreto)