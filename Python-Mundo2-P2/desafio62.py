'''
    desafio 62
	Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
	O programa encerra quando ele disser que quer mostrar.0 termo

'''

num = int(input('Digite um numero :'))
razao = int(input('Digite a Razão :'))
termo = num
contador = 1
total = 0
mais = 10
while mais != 10:
    total = total + mais
    while contador <= total:
        print('{}'.format(termo), end=" ")
        termo += razao  # soma o valor fornecido na variavel razao fora do laco while
        contador += 1   # conta a quantidade de repeticao informada na variavel contador no laço while

        print('\nPAUSA')
        mais = int(input('Quantos termos voce quer mostrar a mais :'))
    print('FIM')
