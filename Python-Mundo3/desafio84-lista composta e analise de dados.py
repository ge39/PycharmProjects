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

    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    resp = str(input("Quer continuar: ")).upper()

    if resp not in "sS":
        break
print(f'Total de pessoas cadastradas: {len(lista)} pessoas')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
        print()
        print(f'tem o menor peso de {menor}')
    elif p[1] == maior:
        print(f'{p[0]} ', end='')
        print()
        print(f'tem maior peso de {maior}')
print('=-' * 30)


