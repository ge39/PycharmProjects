'''
    crie um programa, onde o usuario possa digitar varios valores numericos
    e cadastre-os em uma lista. Caso o numero já exista lá dentro.
    Ele não será adicionado.
    No final, serão exibidos todos os valores unicos digitados em ordem crescente
'''
valor = []
continuar ='S'
while True:
    num = int(input('Digite um numero :'))
    continuar = str(input('Deseja continuar : [S/N]'))
    if num in valor:
        print('nunero ja existe')
    else:
      valor.append(num)
    if continuar not in 'Ss':
        break
print(valor)
print('Fim do Programa')
