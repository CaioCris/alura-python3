import random

def jogar_adivinhacao():
    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    numero_secreto = round(random.randrange(1,101)) #Numeros entre 1 e 100
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('1- Fácil\n2- Médio\n3- Difícil')

    nivel = int(input('Escola o nível: '))

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 5
    else:
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
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if maior:
                print('Errou! Você chutou muito alto!')
            elif menor:
                print ('Errou! Você chutou muito baixo')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = (pontos - pontos_perdidos)

    print('Fim do jogo')
    # print(numero_secreto)

if __name__ == '__main__':
    jogar_adivinhacao()