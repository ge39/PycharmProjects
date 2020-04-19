"""
Faca um programa que ajude o jogador da mega sena criar palpites,
O programa vai perguntar quantos jogos serao gerados
e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""
from random import randint
from time import sleep
lista = list()
jogos = list()

print('-='* 30)
print('\033[31m                Joga na Mega Sena\033[m          ')
print('-='*30)

quant = int(input('Quantos jogos quer que eu sorteie?: '))
tot = 1
while tot <= quant:             # executa o loop até atingir o numero informado pelo usuario
    cont = 0
    while True:
        num = randint(1, 60)    # executa o random de numeros de 1 até 60
        if num not in lista:    # se o numero nao estiver na lista adicione-o
            lista.append(num)
            cont += 1           # contador de numeros da randomização
        if cont >= 6:           # verificar se atingiu o numero de sequencia de 1 até 6
            break
    lista.sort()                # ordena a lista em ordem decrescente
    jogos.append(lista[:])      # faz uma copia da lista para a lista jogos
    lista.clear()               # limpa as duas listas
    tot += 1
print('-='*3, f'Sorteando {quant} Jogos', '-=' *3)  # quantidade de jogos que foi informado

for i, l in enumerate(jogos):                       # exibe o index  da lista e os numeros sorteados
    print(f'jogo {i+1}: {l}')
    sleep(0.75)                                     # timer de exibição, menos de um segundo
print('-='*5, '< BOA SORTE > ', '-='*5)




