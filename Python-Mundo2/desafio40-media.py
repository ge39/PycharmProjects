#crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, e acordo com a média atingida

#-media abaixo de 5.0:
#reprovado
#média entre 5.0 e 6.9:
#recuperação
#média 7.0 ou superior
#aprovado

n1 = float(input('Primeira nota :'))
n2 = float(input('Segunda nota :'))
result = (n1 + n2)/2
if result < 5:
    print('Sua média é\033[31m {}\033[m, \033[31mVocê foi reprovado\033[m'.format(result))
elif result == 5 or result <= 6.9:
    print('Sua média é \033[32m{}\033[m , Voce está de \033[32mrecuperação\033[m'.format(result))
else:
    print('\033[32mAprovado - \033[m' * 5, sep='-', end='')
    print('\033[32mAprovado\033[m')
    print('Sua média é {}, Voce está aprovado'.format(result))
