'''
    tupla = ()
    lista = []
    Lista
'''

lanche = ['Hamburgeur','Suco', 'Pudim', 'Leite']
lanche[3] = 'Chocolate'
print(lanche)
print('=' *40)
print('\033[31mAPPEND\033[m - adiciona um elemento no final da fila')

lanche.append('Queijo')
print(lanche)

print('='*40)
print('\033[31mINSERT\033[m - adiciona um elemento em qualquer posicao da lista')
lanche.insert(0, 'Coco')
print(lanche)

print('='*40)
print('\033[31mdel\033[m - apaga um elemento da lista pelo index')
del lanche[3]
print(lanche)