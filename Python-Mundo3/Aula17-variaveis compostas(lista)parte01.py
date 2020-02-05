'''
    tupla = ()
    lista = []
    dicionario {}
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
print('\033[31mDEL\033[m - apaga um elemento da lista pelo index usando a chave')
del lanche[3]
print(lanche)

print('='*40)
print('\033[31m pop\033[m - por padrão apaga o ultimo elemento ou um elemento da lista adicionando um parametro ao indice')
print(lanche.pop(3))
print('='*40)
print('\033[31m REMOVE\033[m - elimina o elemento pelo seu conteudo, Nome do Objeto')
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
print('='*40)
print('\033[31madicionando o elemento "7" na lista, usando o metodo append,\no elemento é acdicionado no final da lista\033[m')
num = [1, 3, 5, 9]
print(num)
num[3] = 0
num.append(7)
print(num)
print('='*40)
print('contando os elementos')
print(f'Alista tem um total de {len(num)} elementos')

print('='*40)
print('\033[31m INSERT\033[m - Adicionando valores com o metodos insert em qualquer posição')
num.insert(2, 10)
print(num)
print('='*40)
print('\033[31mPOP\033[m - Remoção de elemento usando o indice')
num.pop(4)
print(num)
print('*'*40)
print('\033[31mPOP\033[m - Remoção de elemento sem utilização de index,\npor padrão o ultimo elemento e removido da lista')
num.pop()
print(num)
print('='*40)
print('\033[31mREMOVE\033[m - Percorre a lista e deleta a primeira ocorrencia que for encontrada')
num.remove(10)
print(num)
print('\033[32m =\033[m'*40)
print('Novos Exercícios')

valores = [] # lista vazia ou valores = lista ()
valores.append(5)
valores.append(9)
valores.append(4)
print('Criando um for para formatar a lista de valores')
for v in valores:
    print(f'{v}...')

print('='*40)
print('Exibindo o indice de cada valor usando o enumerate')

for c, v in enumerate(valores):
    print(f'Na posição\033[32m {c}\033[m encontrei o valor \033[31m{v}\033[m')
print('Cheguei ao final da lista')
print('='*40)
print('Adicionando os valores vindo do teclado na lista ')
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor :')))
for c, v in enumerate(valores):
    print(f'Para cada posição\033[34m {c}\033[m temos o valor \033[35m{v}\033[m')
print('Cheguei ao final')





