#  faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int(input('Digite um numero :'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m {}'.format(c), end=' ')
    else:
        print('\033[31m {}'.format(c), end=' ')
