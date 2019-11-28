#  faca um programa que calcule a soma entre todos numeros impares que sao multiplos de tres
#  e que se encontram no  intervalo de 1 até 500
soma = 0
for c in range(1, 500, 2):
    soma = (soma + c)
    print(c, end='-')
print('\n\033[34mA soma de todos os numeros é {}\033[m'.format(soma))
