'''
    Crie um programa, onde o usuario possa adicionar 5 valores numericos e cadastre-os em uma lista
    já na posição correta de inserção, (sem usar o sort()).
    No final, mostre a lista ordenada na tela.

'''
lista = []

while True:
    num = (int(input('Digite um Numero')))
    resp = str(input('Deseja continuar [S/N] '))

    if resp in 'nN':
        break
    if num == 0:
        lista.append(num)
        print(f'Numero {num} adicionado no final da lista')
        print(len(lista))
    else:
        print('menor')
