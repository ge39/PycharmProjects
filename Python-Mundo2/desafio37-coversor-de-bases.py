#escreva um programa que leia um numero inteiro qualquer e peça para o usuario
#escolhar qual será a base de conversao:

# 1-para binario
# 2-para octal
# 3-para hexadecimal

num = int(input('Digite um numero :'))
base = str(input('Escolha uma base,\033[33moctal\033[m,\033[34mbinario\033[m,\033[31mhexadecimal\033[m :')).upper().strip()

if base == 'HEXADECIMAL':
    print(base)
elif base == 'BINARIO':
    print(base)
else:
    print(base)
