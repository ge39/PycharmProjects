"""
Faca um programa que leia o nome e peso de varias pessoas,
guardando tudo em uma lista e no final mostre:

A - Quantas pessoas foram cadastradas
B - Uma listagem com as pessoas mais pesadas
C - Uma listagem com as pessoas mais leve

"""
pessoa = []
pesopessoa = []
lista = []
cont = 0
while True:
    nome = str(input("Digite o nome: ")).upper().strip()
    peso = int(input("Qual o peso: "))
    pessoa.append(nome)
    pessoa.append(peso)
    lista.append(pessoa[:])
    resp = str(input("Quer continuar: ")).upper()
    cont+=1
    if peso  < peso:
        pesopessoa.append(peso)
        print(f'Maior peso {pesopessoa}')
    if resp not in "sS":
        break
print(f'Total de pessoas cadastradas: {cont} pessoas')
# print(f'O maior peso foi {mais} e o menor foi {menos}')
print('=-' * 30)

