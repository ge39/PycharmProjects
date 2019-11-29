#  faca um programa que calcule a soma entre todos numeros impares que sao multiplos de tres
#  e que se encontram no  intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = (soma + c)
        cont = cont + 1
        print(c, end='-')
print('\n\033[34mA soma dos {} valores é {}\033[m'.format(cont, soma))
