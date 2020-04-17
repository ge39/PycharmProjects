""""
Crie um programa que o usuario possa digitar 7 valores numericos
e cadastre-os em uma lista unica que mantenha separado os valores pares e impares
No final mostre os valores pares e impares em ordem crescente
"""
num = []
for v in range(0, 7):
    num.append(float(input(f"Digite o {v + 1}º numero: ")))
print(num)

for par in num:
    if par % 2 == 0:
        print('Par :', end='')
        print(f'{par}\n ', end='')

for impar in num:
    if impar % 2 == 1:
        print('Impar :', end='')
        print(f'{impar}\n ', end='')


