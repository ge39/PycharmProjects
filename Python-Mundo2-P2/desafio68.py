'''
    Faça um programa que jogue par ou impar om o computador
    o jogo será interrompido quando o jogador perder
    mostrando o total de vitórias consecutivas
    que ele conquistou no final do jogo
'''

from random import randint
p = i = num = jogada = vitoria = derrota = 0
computador = randint(0, 6)
continuar = 'S'

while continuar in 'sS':
    num = int(input('Digite um numero :')[0])
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
            derrota +=1
        continuar = str(input('Deseja Continuar [S] Sim e [N] Não :'))
    if soma % 2 != 0:
        jogada += 1
        if acao in 'Pp':
            print(f'{soma} é impar e voce Perdeu')
            derrota += 1
        else:
            print(f' {soma} é impar e voce Venceu')
            vitoria += 1
        continuar = str(input('Deseja Continuar [S] Sim e [N] Não :'))
    if continuar in 'nN':
        print('*'*20)
        print(f'\033[34mTotal de jogadas {jogada}\033[m\n\033[31mCOMPUTADOR: {derrota}\033[m\n\033[32mJOGADOR: {vitoria} \033[m')
        print("FIM de JOGO")

        if vitoria > derrota:
            print('\033[32mPARABENS, VOCE É O VENCEDOR !!!\033[m')
        elif vitoria == derrota:
         print('\033[32mHOUVE EMPATE !!\033[m')
        else:
            print('\033[31mO COMPUTADOR GANHOU !!\033[m')
        print('*' * 20)
