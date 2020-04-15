'''
    Crie um programa que leia varios numeros e coloque em uma lista
    depois disso mostre:

    A - Quantos numeros foram digitados
    B - A lista de valores ordenados de forma decrescente
    C - Se o valor 5 foi digitado e está ou não na lista
'''
from itertools import count

lista = []
cont = 0
num = 1
while num != 0:
    num = int(input("Digite um numero :"))
    lista.append(num)
    cont += 1

print(f'Total de numeros digitados: {cont} numeros')
lista.sort(reverse=True)
print(f'Lista de valores decrescente {lista}')

if 5 in lista:
    print(f'O numero 5 aparece na lista {lista.count(5)} vezes')
else:
    print('O numero 5 nao aparece na lista')
