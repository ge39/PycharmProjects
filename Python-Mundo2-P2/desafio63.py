'''
    desafio 63
	Escreva um prodgrama que leia um numero N inteiro qualquer e mostre na tela
	Os N primeiros elementos de uma sequenca de  Fibonacci

	ex:0 -> 1 -> 2 -> 3 -> 5 -> 8
'''
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos voce quer mostra ?'))
t1 = 0
t2 = 1

print('-'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
else:
    print('\033[31m\nFIM\033[m')


