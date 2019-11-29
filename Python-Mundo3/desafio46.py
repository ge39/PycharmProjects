#  faça um perograma que mostre na tela uma:
#  contagem regressiva para o estouro de fogos de artificios
#  indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep
for cont in range(10, -1, -1):
    sleep(1)
    print(cont, sep='-', end='-')
print('\033[34m=FELIZ NATAL\033[m'*2)
