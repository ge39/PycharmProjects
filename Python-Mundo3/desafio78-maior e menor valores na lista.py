'''
  faça um programa que leia 5 valores numericos e guarde em uma lista
  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
'''
numero = maior = menor = 0

listanum = []

for c in range(0, 5):
    listanum.append(int(input('Digite um Valor: ')))
if c == 0:
       maior = menor = listanum[c]
else:
   if listanum[c] > maior:
       maior = listanum[c]
   if listanum[c] < menor:
        menor = listanum[c]
print(f'O Menor valor da lista é {menor}/nO maior valor é {maior}')

