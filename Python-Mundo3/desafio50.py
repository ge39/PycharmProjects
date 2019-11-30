#  desenvolva um sistema que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#  se o valor digitado for impar, desconsidere-o
soma = 0
for c in range(1, 7):
    var = c
    num = int(input('Digite o {}º numero:'.format(var)))

    if num % 2 == 0:
        #print(num)
        soma += num
print('Soma dos numero pares são {}'.format(soma))
