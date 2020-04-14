'''
    Crie um programa, onde o usuario possa adicionar 5 valores numericos e cadastre-os em uma lista
    já na posição correta de inserção, (sem usar o sort()).
    No final, mostre a lista ordenada na tela.

'''
lista = []
for c in range(0, 5):
    num = (int(input('Digite um Numero: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado o numero {num} ao final da lista')
    else:
        index = 0
        while index < len(lista):
            if num <= lista[index]:
                lista.insert(index, num)
                a = len(lista)
                print(f'Lista len {a}')
                print(f'Adicionado o numero {num} na posicao {index} da lista e {lista}')
                break
            index += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram  {lista}')

