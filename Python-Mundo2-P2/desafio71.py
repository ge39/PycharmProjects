'''
    Crie um programa que simule o funcionamento de um caixa eletronico.
    No inicio, pergunte ao cliente qual o valor a ser sacado (numero inteiro)
    e o programa irá informar quantas cedulas de cada valor serão entrgues
    OBS: considere que o caixa possui cedulas R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$1,00
'''
saldo = int(100.00)
while True:
    print('*'*60)
    saque = int(input('Quanto quer sacar ? R$:'))

    if saque <= saldo:
        saldo -= saque
        print(f'Saque autorizado!!!\nSaldo Anterior: R${saldo + saque:.2f}\nValor do Saque: R${saque:.2f}\nSaldo Atualizado R${saldo:.2f}')
    else:
        break
print(f'O saque de R${saque:.2f} nao foi autorizado, Seu saldo é menor, R${saldo:.2f}')
