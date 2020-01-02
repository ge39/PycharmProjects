'''
    crie um programa que leia o nome e o preço de varios produtos
    O programa  deverá perguntar se o usuario vai continuar, e no final mostre

    A - Qual é o total gasto na compra
    B - Quantos produtos custam mais de R$ 100,00
    C - Qual o nome do produto mais barato
'''
pergunta = 'S'
total = qtde = vproduto = 0
maiscaro = maisbarato = 0

while pergunta in 'sS':
   desc = str(input('Qual a descrição do Produto :')).strip().upper()
   valor = float(input('Qual o valor do Produto R$:'))
   pergunta = str(input('Deseja adicionar mais produtos na cesta? :'))
   total += valor
   maiscaro = valor
   maisbarato = valor

   if valor > 100:
        qtde += 1
   if valor > maiscaro:
        maiscaro = valor
   elif valor <= maisbarato:
        maisbarato = valor
        desc
else:
        print('*'*60)
        print(f'Valor total gasto R$ {total:.2f}')
        print(f'Na cesta tem  {qtde} produtos , que custa mais de R$ 100.00')
        print(f'O produto mais barato é {desc}')
