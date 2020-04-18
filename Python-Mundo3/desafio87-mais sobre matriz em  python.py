"""
Aprimore o desafio anterior, mostrando no final
A - A soma de todos os valores pares
B - A soma dos valores da terceira coluna
C - O maior valor da segunda linha
 """

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
scol = spar = 0
for l in range(0, 3):
    for c in range(0, 3):
       matriz[l][c] = int(input(f'Digite [{l}, {c}] :'))
print('=-' *40)
for l in range(0, 3):
    for c in range(0, 3):
       print(f'[{matriz[l][c]:^5}]', end='')
       if matriz[l][c] % 2 == 0:
           spar += matriz[l][c]
    print()
print('-=' *40)
print(f'Soma dos valores pares é {spar}.', end='')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'\nA soma dos valores da 3ª coluna é {scol}.')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é {maior}.')

for c in range(0, 3):
    for l in range(0, 3):
        if c == 0 and l == 0:
            mai = matriz[l][c]
        elif matriz[l][c] > mai:
            mai = matriz[l][c]
print(f'\033[31mO maior numero da matriz é {mai}\033[m')

