#  tuplas
#  listas
#  dicionarios

#   TUPLAS
#   as tuplas são imutaveis - poderia ser uma constante
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim','Batata Frita')

print(lanche[0:3])
print(lanche[-4])
print(lanche[0:])
print(lanche[3:])
print(lanche[:])
print('*'*30)
print(lanche)
print('*'*30)
for c in lanche:
    print(len(c))
    print(c[0:3])
print('*'*30)
for cont in range(0, len(lanche)):
    print(cont)
print('*'*30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('*'*30)
for cont in range(0, len(lanche)):
    print(lanche[cont])

