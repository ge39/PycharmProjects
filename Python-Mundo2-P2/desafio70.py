'''
    crie um programa que leia o nome e opreço de varios produtos
    O programa  deverá perguntar se o usuario vai continuar, e no final mostre

    A - Qual é o total gasto na compra
    B - Quantos produtos custam mais de R$ 100,00
    C - Qual o nome do produto mais barato
'''
pergunta = 'S'
valor = total = qtde = vproduto = 0
maiscaro = maisbarato = 0

while pergunta in 'sS':
   desc = str(input('Qual a descrição do Produto :')).strip().upper()
   valor = float(input('Qual o valor do Produto R$:'))
   pergunta = str(input('Deseja adicionar mais produtos na cesta? :'))
   total += valor

   if valor > 100.00:
      qtde += 1
      vproduto = valor
      descricao = desc
    if valor < maiscaro:
       maisbarato = valor
    elif valor > maiscaro:

else:
       print('*'*60)
       print(f'Valor total gasto R$ {total:.2f}')
       print(f'Na cesta tem  {qtde} produtos , que custa {vproduto:.2f} e é o maior valor da cesta')

