'''
    desafio 62
	Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
	O programa encerra quando ele disser que quer mostrar.0 termo

'''

num = int(input('Digite um numero :'))
razao = int(input('Digite a Razão :'))
termo = num
contador = 0
continua = 'S'
while continua in 'S':
    while contador <= 10:
        print('{}'.format(termo), end=" ")
        contador += 1   # conta a quantidade de repeticao informada na variavel contador no laço while
        termo += razao  # soma o valor fornecido na variavel razao fora do laco while

    cont = str(input('\nDeseja lançar outro termo :'))
    if continua in 'Ss':
        num1 = int(input('Digite um numero :'))
        razao1 = int(input('Digite a Razão :'))
        termo1 = num1
        contador1 = 0

        print('{}'.format(termo1), end=" ")
        contador1 += 1  # conta a quantidade de repeticao informada na variavel contador no laço while
        termo1 += razao1  # soma o valor fornecido na variavel razao fora do laco while
    else:
        print('FIM')
        break