'''
  faça um programa que leia 5 valores numericos e guarde em uma lista
  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
'''
numero = maior = menor = 0
listanum = []
for c in range(0, 5):
    listanum.append(int(input('Digite um Valor: ')))
    if c == 0:#  Se for inicio do laço faça ....
        maior = listanum[c]
        menor = listanum[c]
    else:# Se não for o inicio do laço, então ......
        if listanum[c] > maior:
           maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Lista total {listanum}')
print(f'O Menor valor da lista é : {menor}\nO maior valor da lista é : {maior}')

