'''
    Crie um programa que tenha uma tupla com varias palavras
    (não usar acentos).
    Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
'''

palavras = ('java script', 'Python', 'Php', 'Java', 'Ruby', 'Html', 'Mysql')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ',end='')
    for letra in p:
      if letra.lower() in 'aeiou':
        print(f'\033[34m{letra}\033[m', end=' ')
