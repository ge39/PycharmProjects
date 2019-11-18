#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

#Se ele ainda vai se alistar ao servico militar
#se é hora de se alistar
#se ja passou da hora de se alistar

#seu programa deve mostrar tambem o tempo que falta ou que passou do prazo

from datetime import date
idade = int(input('Qual sua idade :'))
ano = date.today().year
nascido = ano -idade
print('Voce nasceu no ano de {}'.format(nascido))
anoalistar = ano - 18
print('\033[33mAlistamento para nascidos no ano de {}\033[m'.format(anoalistar))

if anoalistar == nascido:
        print('\033[34mVoce tem {} anos e está apto ao serviço militar\033[m'.format(idade))
elif anoalistar > nascido:
    print('Voce tem {} anos e está atrasado em {} anos '.format(idade, anoalistar-nascido))
else:
    print('\033[31mVoce tem {} anos, e precisa esperar mais {} ano\033[m'.format(idade,nascido-anoalistar))

