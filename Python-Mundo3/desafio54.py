#  crie um programa que leia o ano de nascimento de 07 pessoas.
#  no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores
from datetime import date
soma = 0
for c in range(1, 8):
    nasc = int(input(' {}º Digite o ano de nascimento :'.format(c)))
    atual = date.today().year
    maioridade = atual - nasc
    #print(maioridade)
    if maioridade >=21:
        print('Voce tem {} anos e é maior de 21 anos'.format(maioridade))
        soma = soma + 1
        print(soma)
    #else:
        #print('Você tem {} anos e não alcançou a maioridade'.format(maioridade))
