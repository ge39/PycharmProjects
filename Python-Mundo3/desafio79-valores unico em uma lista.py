'''
    crie um programa, onde o usuario possa digitar varios valores numericos
    e cadastre-os em uma lista. Caso o numero já exista lá dentro.
    Ele não será adicionado.
    No final, serão exibidos todos os valores unicos digitados em ordem crescente
'''
valores = 0
continuar ='S'
while True:
    num = int(input('Digite um numero :'))
    continuar = str(input('Deseja continuar : [S/N]'))
    num.insert(num)
    if continuar not in 'Ss':
        break
print(num)
print('Fim do Programa')
