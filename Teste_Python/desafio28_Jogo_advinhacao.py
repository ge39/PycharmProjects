#escreva um programa que faça o computador pensar
#entre um numero entre zero e cinco, e peca para o usuario tentar descobrir
#qual foi o numero escolhido pelo computador.
#o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice
lista = (0, 1, 2, 3, 4, 5)
escolhido = choice(lista)

numero = int(input('digite um numero :'))
print('Processando....')
if numero == escolhido:
    print('Parabens, o numero escolhido foi {}'.format(escolhido))
else:
    print('voce errou, o numero escolhido foi {}'.format(escolhido))



