'''
    Crie um programa que vai ler varios numeros e colocar em uma lista
    Depois disso,
    Crie duas listas extras que vao conter apenas os valores pares
    e os valores impares digitados, respectivamente.
    Ao final mostre o conteudo das 3 listas geradas
'''
lista = []
par = []
impar = []
n = 1

while n != 0:
    n = int(input("Digite um valor :"))
    lista.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Lista geral dos valores {lista}')
print(f'Lista dos numeros pares {par}')
print(f'Lista dos numeros impares {impar}')


