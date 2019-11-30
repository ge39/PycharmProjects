#  desenvolva um sistema que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#  se o valor digitado for impar, desconsidere-o
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º numero:'.format(c)))
    if num % 2 == 0:
       soma += num
       cont = cont + 1
print('Total dos numeros pares {}, e sua soma é {}'.format(cont, soma))
