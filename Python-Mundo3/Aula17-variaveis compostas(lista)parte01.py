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
print('\033[31mdel\033[m - apaga um elemento da lista pelo index usando a chave')
del lanche[3]
print(lanche)

print('='*40)
print('\033[31m pop\033[m - por padrão apaga o ultimo elemento ou um elemento da lista adicionando um parametro ao indice')
print(lanche.pop(3))
print('='*40)
print('\033[31m remove\033[m - elimina o elemento pelo seu conteudo, Nome do Objeto')
if 'Suco' in lanche:
    print(lanche.remove('Suco'))
print(lanche)
print('='*40)
print('criando lista através de um range ordenada de forma crescente ou reversa')
valores = list(range(4, 11))
valores.sort(reverse=True)
print('ordem reversa ou decrescente')
print(valores)
valores.sort()
print('='*40)
print('ordem crescente')
print(valores)




