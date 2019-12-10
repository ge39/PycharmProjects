'''
    desafio 59
	crie um programa que leia 2 valores e mostre um menu na tela:
	[1] somar
	[2] multiplicar
	[3] maior
	[4] novos numeros
	[5] sair do programa

	seu programa deverá realizar a operação solicitada em cada caso.
'''
num1 = int(input('Digite o Primeiro numero :'))
num2 = int(input('Digite o Segundo numero :'))

print('''
    [1] somar
	[2] multiplicar
	[3] maior
	[4] novos numeros
	[5] sair do programa

''')

num = 1
while num < 5:
    digite = int(input('Digite um numero do Menu :'))
    if digite == 1:
        print(num1 + num2)
    if digite == 2:
        print(num1 * num2)
    if digite == 3:
        if num1 > num2:
            print('O valor {} é maior que o valor {}'.format(num1, num2))
        else:
            print('O valor {} é maior que o valor {}'.format(num2, num1))