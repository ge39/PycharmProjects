'''
    desafio 65
	Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução mostre :
	a media entre todos valores
	qual foi o maior e o menor valores lidos.

	o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
'''
continuar = 'S'
cont = n = media = maior = menor = 0

while continuar == 'S':
    n = int(input('Digite um numero : '))
    continuar = str(input('Deseja continuar [S/sim] [N/não] :')).upper()
    cont += 1
    n += n
    media = n/cont
else:
    print('\033[31mTotal de numeros {}\033[m \n\033[32mSoma dos valores {:.2f}\033[m \033[34m \ne a sua média {:.2f}\033[m'.format(cont, n, media))