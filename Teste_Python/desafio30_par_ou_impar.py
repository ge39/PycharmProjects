#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

num = int(input('digite um numero :'))
resultado = num % 2

print('esse número é par' if resultado == 0 else 'esse numero é impar')