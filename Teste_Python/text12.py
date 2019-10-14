#faça um programa que leia a largura e a altura de uma parede em metros,
#calcule sua área e a quantidade de tinta necessária para pinta-la.
#sabendo que, cada litro de tinta, pinta uma área de 2m2

altura = float(input('Digite a Altura :'))
largura = float(input('digite a largura :'))
print("Total da Área :", (altura * largura),"/n Total de latas de tinta: ",(altura * largura / 2))
