'''
    Faça um programa que jogue par ou impar om o computador
    o jogo será interrompido quando o jogador perder
    mostrando o total de vitórias consecutivas
    que ele conquistou no final do jogo
'''

from random import randint
p = i = num = jogada = vitoria = 0
computador = randint(0, 6)
continuar = 'S'

while continuar in 'sS':
    num = int(input('Digite um numero [6] para finalizar:')[0])
    acao = str(input('Voce quer par [p] ou impar[i] :'))
    soma = computador + num
    #  print(f'A soma de {num} e {computador} é {soma}')

    if soma % 2 == 0:
        jogada += 1
        if acao in 'Pp':
            print(f'{soma} é par e voce Venceu ')
            vitoria += 1
        else:
            print(f'{soma} é par e voce Perdeu ')
        continuar = str(input('Deseja Continuar [S] Sim e [N] Não :'))
    if soma % 2 != 0:
        jogada += 1
        if acao in 'Pp':
            print(f'{soma} é impar e voce Perdeu')
        else:
            print(f' {soma} é impar e voce Venceu')
            vitoria += 1
        continuar = str(input('Deseja Continuar [S] Sim e [N] Não :'))
    if continuar in 'nN':
        print(f'\033[34mTotal de jogadas {jogada}\033[m\n\033[33mVitoria {vitoria} vez(es)\033[m')
        print("FIM de JOGO")
