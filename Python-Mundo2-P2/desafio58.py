'''
    desafio 58
	Melhore o jogo do desafio 28, onde o computador vai 'PENSAR', em um numero entre 0 e 10.
	só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos
	palpites foram necessarios para vencer
'''

from random import randint
contar = 0
computador = randint(0, 10)
jogador = int(input('Digite o numero que pensei :'))

while jogador != computador:
    if jogador != computador:
        jogador = int(input('Digite o numero que pensei :'))
        contar += 1
else:
    print('Parabéns, eu pensei no numero {} , mas voce preciso de {} tentativa'.format(computador, contar))

