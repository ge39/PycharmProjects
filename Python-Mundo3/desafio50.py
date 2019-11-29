#  desenvolva um sistema que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#  se o valor digitado for impar, desconsidere-o
for c in range(1, 7):
    var = c
    num = int(input('Digite o {}º numero:'.format(var)))
soma = 0
for n1 in range(0, 7, 2):
    soma += n1
print(soma)