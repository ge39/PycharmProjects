'''
  faça um programa que leia 5 valores numericos e guarde em uma lista
  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
'''
numero = maior = menor = 0
for num in range(0, 5):
    numero = int(input(f'Digite um numero na posição {num}:'))
    if num == 0:
        maior = numero
        menor = numero

    else:
        if numero >= maior:
            maior = numero
            pmaior = num
        elif numero <= menor:
            menor = numero
            pmenor = num
print(f'o numero maior é {maior} na posição {pmaior}\nO numero menor é {menor} na posição ')


