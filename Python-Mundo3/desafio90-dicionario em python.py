'''
Faça um programa que leia nome e média de um aluno.
guardando tambem a situação em um dicionario.
No final, mostre o conteudo da estrutura na tela
'''
aluno = {}


aluno['nome'] = str(input('Nome: ').upper())
aluno['media'] = float(input(f'Média {aluno["nome"]}: '))


if aluno['media'] >= 5:
    aluno['situacao'] = 'Aprovado'
    #print(f'Aluno Aprovado')
elif 4 <= aluno['media'] < 5:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
     if aluno['situacao'] == 'Reprovado':
        print(f'{k} é igual \033[31m{v}\033[m')
     else:
         print(f'{k} é igual \033[34m{v}\033[m')

