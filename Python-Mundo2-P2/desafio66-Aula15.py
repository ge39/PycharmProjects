'''
    crie um programa que leia varios numeros inteiros pelo teclado.
    o programa só vai parar quando o usuário digitar o valor 999. que é a condição de parada
    no final, mostre quantos numeros foram digitados e qual foio a soma entre eles
    (desconsiderando o flag)
'''
c = soma = cont = 0
while c != 999:
    c = int(input('Digite um numero [999 para parar]:'))
    if c != 999:
        cont += 1
        soma += c
    else:
        print(f'Numeros digitados foram {cont} e a soma é {soma}')
