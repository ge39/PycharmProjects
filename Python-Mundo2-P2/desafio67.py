'''
    Faça um programa que mostre a tabuaada de varios numeros
    Um de cada vez, para cada valor digitado pelo usuario.
    O programa será interrompido quando numero solicitado for negativo
'''

print('Tabuada')

while True:
    n = int(input('Digite um numero para gerar a tabuada :'))
    print('-' * 60)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-'*60)
