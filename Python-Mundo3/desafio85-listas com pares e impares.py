""""
Crie um programa que o usuario possa digitar 7 valores numericos
e cadastre-os em uma lista unica que mantenha separado os valores pares e impares
No final mostre os valores pares e impares em ordem crescente
"""
# Lista e sublistas
num = [[], []]
for v in range(0, 7):
    valor = float(input(f"Digite o {v + 1}º numero: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 40)
num[0].sort()
num[1].sort()
print(f'\033[34mTotal de {len(num[0] + num[1])} numeros digitados\033[m')
print(f'Os valores pares sao {num[0]}')
print(f'Os valores impares sao {num[1]}')

