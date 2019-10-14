#desenvolva um programa que leia um numero e
# mostre o seu dobro, triplo e raiz quadrada

nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
media = float((nota1 + nota2) / 2)
raiz = (media**(1/2))

print("A média das duas notas é: {}\n Raiz quadrada de: {} é: {:.3f}".format(media,media,raiz))