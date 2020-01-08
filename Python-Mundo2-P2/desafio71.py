'''
    Crie um programa que simule o funcionamento de um caixa eletronico.
    No inicio, pergunte ao cliente qual o valor a ser sacado (numero inteiro)
    e o programa irá informar quantas cedulas de cada valor serão entrgues
    OBS: considere que o caixa possui cedulas R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$1,00
'''
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
saque = int(input('Qual valor quer sacar ? \033[34mR$\033[m '))
total = saque
ced = 100
totced  = 0
while True:
    if total >= ced:  # verifica enquanto o valor do saque for maior ou igual o valor da cedula
       total -= ced   # subtrai o valor da cedula do valor do saque
       totced += 1    # soma o total de cedula para dar o valor do saque ex: R$ 100 = 2 cedulas de R$ 50,00
    else:
        if totced > 0:
          print(f'total de {totced} no valor de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced =0
        if total == 0:
            break
print('FIM')





