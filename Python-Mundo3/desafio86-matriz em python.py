""""
Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lido pelo teclado
No final, mostre a matriz na tela com a formatação correta

"""
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
     for l in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]:'))

print(matriz, end='')
print()

