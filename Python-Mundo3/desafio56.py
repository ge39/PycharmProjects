#  desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
#  no final do  programa, mostre:
#  a media de idade do grupo
#  o nome do homem mais velho
#  quantas mulheres tem menos de 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'========= {p}ª Pessoa =======')
    nome = str(input('Nome   da {}ª Pessoa :'.format(p))).strip().upper()
    idade = int(input('idade  da {}ª pessoa :'.format(p)))
    sexo = str(input('Sexo   da {}ª pessoa [M/F] :'.format(p))).strip().upper()
    print('')
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo {:.2f}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} o total de mulheres com menos de 20 anos'.format(totmulher20))