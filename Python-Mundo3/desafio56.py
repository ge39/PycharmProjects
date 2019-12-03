#  desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
#  no final do  programa, mostre:
#  a media de idade do grupo
#  o nome do homem mais velho
#  quantas mulheres tem menos de 20 anos

for p in (1, 5):
    print('======={}ª Pessoa=======')
    nome = str(input('Nome da {}ª Pessoa :'.format(p)))
    idade = int(input('idade da {}ª pessoa'.format(p)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]'.format(p))).strip()