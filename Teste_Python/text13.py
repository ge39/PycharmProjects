#faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço com 5 % de desconto

preco = float(input('digite o valor :'))
desconto = float(input('digite o valor do desconto :'))
print("o novo valor com desconto é : ",(preco * desconto / 100) - preco)