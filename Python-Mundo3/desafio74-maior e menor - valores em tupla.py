'''
    Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla
    Depois disso, mostre a listagem de numeros gerados e tambem indique
    o menor eo maior valor que estão na tupla
'''
cont = 1
from random import randint
while cont <= 5:
    lista = randint(10, 15)
    cont += 1
print(f'{lista}')
