'''
    Faça um programa que mostre a tabuaada de varios numeros
    Um de cada vez, para cada valor digitado pelo usuario.
    O programa será interrompido quando numero solicitado for negativo
'''

print('Tabuada')

numerador = result = 0
multiplicador = int(input('Digite um numero para gerar a tabuada :'))
m = multiplicador
parada = 0

while True:
    numerador += 1
    result = multiplicador * numerador
    print(f'{m} X {numerador} = {result}')
    if numerador == 10:
        numerador = result = 0
        multiplicador = int(input('Digite um numero para gerar a tabuada :'))
        m = multiplicador
        print(f'{m} X {numerador} = {result}')
        numerador += 1
        result = multiplicador * numerador

