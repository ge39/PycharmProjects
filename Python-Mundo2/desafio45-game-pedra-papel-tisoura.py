from time import sleep
from random import randint
itens = ('pedra','papel', 'tesoura')
computador = randint(0,2)
print('''
    [0 Pedra
    [1] Papel
    [2] Tesoura''')
jogador = int(input('Qual é  a sua jogada? :'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('\033[32m-=\033[m'*20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('\033[32m-=\033[m'*20)

if computador == 0:
    if jogador == 0:
        print('')
    elif jogador == 1:
        print('')
    elif jogador == 2:
        print('')
else:
    print('JOGADA INVÁLIDA!!!')

elif computador == 1:
if jogador == 0:
    print('')
    elif jogador == 1:
    print('')
    elif jogador == 2:
    print('')
else:
    print('JOGADA INVALIDA')
elif computador == 2:
    print('')
else
    print('JOGADA INVÁLIDA!!!')
