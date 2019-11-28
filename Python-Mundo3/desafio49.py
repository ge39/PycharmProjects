#  refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher.
#  só que agora utilizarei um laço for

num = int(input('Digite a tabuada :'))
for c in range(1, 11,):
    print(num, 'x', c, '= {}'.format(c * num))
