#  crie um programa que leia o ano de nascimento de 07 pessoas.
#  no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores
from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year

for c in range(1, 8):
    nasc = int(input(' {}º Digite o ano de nascimento :'.format(c)))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print('Você tem {} pessoas maiores de 21 anos'.format(totmaior))
print('Você tem {} pessoas menores de 21 anos'.format(totmenor))
