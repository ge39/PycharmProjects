"""
Faca um programa que leia o nome e peso de varias pessoas,
guardando tudo em uma lista e no final mostre:

A - Quantas pessoas foram cadastradas
B - Uma listagem com as pessoas mais pesadas
C - Uma listagem com as pessoas mais leve

"""
pessoa = []
lista = []
maior = menor = 0

while True:
    pessoa.append(str(input("Digite o nome: ").upper().strip()))
    pessoa.append(float(input("Qual o peso: ")))

    if len(lista) == 0:  # se a lista for vazia faça...
        maior = menor = pessoa[1]   # o maior peso e o menor peso será o primeiro peso digitado
    else:                           # se a lista não for vazia faça...
        if pessoa[1] > maior:       # se o peso digitado for maior que o peso armazenado na variavel "maior"
            maior = pessoa[1]       # a variavel maior recebe o valor digitado pelo usuario
        if pessoa[1] < menor:       # se o peso digitado for menor que o peso armazenado na variavel "menor"
            menor = pessoa[1]       # a variavel menor recebe o valor digitado pelo usuario
    lista.append(pessoa[:])         # é feito uma cópia da lista pessoa para o array lista
    pessoa.clear()                  # os dados das lista pessoa são apagados
    resp = str(input("Quer continuar: ")).upper()

    if resp not in "sS":
        break
print(f'Total de pessoas cadastradas: {len(lista)} pessoas')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')  # imprime o maior peso da pessoa

for p in lista:                                 # criado um ponteiro "p" para ler a posição do array "lista"
    if p[1] == maior:                           # Se o index 1 da lista, "o index 1 representa a lista na posição[1] = peso"
        print(f'{p[0]},', end='')               # imprime o nome da pessoa
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='') # imprime o peso da pessoa
for p in lista:
    if p[1] == menor:                         # se o index 1 for = ao maior peso da lista
        print(f'{p[0]},', end=' ')             # imprime o nome da pessoa
print()



