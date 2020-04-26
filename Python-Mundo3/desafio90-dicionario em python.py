'''
Faça um programa que leia nome e média de um aluno.
guardando tambem a situação em um dicionario.
No final, mostre o conteudo da estrutura na tela
'''
dados = {}

while True:
    dados['nome'] = str(input('Nome: ').upper())
    dados['media'] = float(input('Média: '))

    if dados['media'] >= 5:
        dados['situacao'] = 'Aprovado'
        #print(f'Aluno Aprovado')
        print(dados)
    else:
        dados['situacao'] = 'Reprovado'
       #
        print(dados)