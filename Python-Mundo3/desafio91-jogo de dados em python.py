'''
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário.
    No final , coloque esse dicionario em ordem,sabendo que o vencedor tirou o maior numero no dado
'''
from random import randint
analise = dict()

for j in range(0, 4):
    analise['player'] = j
    # jogadas do dado = 6
    num = randint(1, 7)
    analise['point'] = num
    print(analise)

