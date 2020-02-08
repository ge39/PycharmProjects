'''
  faça um programa que leia 5 valores numericos e guarde em uma lista
  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
'''
numero = maior = menor = 0
pmaior = pmenor = 0
valor = (0, 1, 2, 3, 4)
for pos, num in enumerate(valor):
    numero = int(input(f'Digite um numero na posição {num}:'))
    if num == 0:
        maior = numero
        menor = numero
    else:
        if numero >= maior:
            maior = numero
            pmaior = num
            pmaior = pos
        elif numero <= menor:
            menor = numero
            pmenor = pos
print(f'\033[31mO numero maior é {maior} na posição {pmaior}\033[m\n\033[33mO numero menor é {menor} na posição {pmenor}\033[m')


