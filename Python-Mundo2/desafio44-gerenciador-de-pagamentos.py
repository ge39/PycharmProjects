#  elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#  preço normal e condição de pagamento:

#- a vista dinheiro/cheque: 10% de desconto
#- a vista no cartao: 5% de desconto
#- em até 2 vezes no cartao: preço normal
#- 3 vezes ou mais no cartao: 20% de juros

print('\033[31mForma de pagamento\033[m')
print('\033[34m\n'
      '    1 - DINHEIRO / CHEQUE\n'
      '    2 - CARTÃO DÉBTO\n'
      '    3 - CARTÃO 2 VEZES\n'
      '    4 - CARTÃO ACIMA DE 2 VEZES\033[m')
print('='*100)
valor = float(input('Digite o valor da compra R$ '))

pagto = int(input('Digite a forma de pagamento :'))

if pagto == 1:
    print('Pagamento em dinheiro ou cheque')
elif pagto == 2:
    print('Pagamento no cartão de débito')
elif pagto == 3:
    print('Pagamento em 2 vezes no cartão')
elif pagto == 4:
    print('Pagamento no cartao acima de 2 vezes')
else:
    print('Forma de pagamento \033[31m{}\033[m - inesistente'.format(pagto))