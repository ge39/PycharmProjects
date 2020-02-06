'''
  faça um programa que leia 5 valores numericos e guarde em uma lista
  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
'''
maior = menor = 0
for num in range(0, 5):
 numero = int(input(f'Digite um numero na posição {num}:'))

    if num == 0:
        maior = numero
        menor = numero
    else:
        if maior == numero:
            numero = maior
        if menor == numero:
            numero = menor
print(f'o numero maior é {maior}\n O numero menor é {menor}')


