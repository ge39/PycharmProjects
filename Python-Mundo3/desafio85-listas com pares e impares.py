""""
Crie um programa que o usuario possa digitar 7 valores numericos
e cadastre-os em uma lista unica que mantenha separado os valores pares e impares
No final mostre os valores pares e impares em ordem crescente
"""
num = []
for v in range(0, 7):
    num.append(float(input(f"Digite o {v + 1}º numero: ")))
print(num)

for p in num:
    if p % 2 == 0:
       print(f'par - {p}\n ', end='')

    else:
        print(f'impar - {p}\n ', end='')


