#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e  mostre
#e mostre sua categoria, de acordo com a idade:

#-até 9 anos mirim
#-até 14 anos:infantil
#-até 19 anos: junior
#-até 20 anos: senior
#-acima: master

from datetime import date
ano = date.today().year
nasc = int(input('Ano que nasceu :'))
result = ano - nasc

if result < 10:
    print('voce tem {} anos, sua categoria é Mirim'.format(result))
elif 9 < result and result < 15:
    print('voce te {} anos, sua categoria é Infantil'.format(result))
elif result <= 19 and result > 14:
    print('Voce tem {} anos, Sua categoria é Junior'.format(result))
elif result > 19 and result <= 20:
    print('Voce tem {} anos, sua categoria é Senior'.format(result))
else:
    print('Voce tem {} anos, sua categoria é Master'.format(result))
