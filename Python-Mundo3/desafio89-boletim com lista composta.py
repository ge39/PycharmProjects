"""
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
No final, mostre um boletim contendo a média de cada um e permita que o usuario posso mostrar as notas
de cada aluno individualmente

"""
ficha= []
notas = list()
while True:
    nome = str(input("Nome: ").upper().strip())
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input("Deseja continuar [S/N] "))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 26)
for i, a in enumerate (ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input("Mostar as notas de qual aluno? (999) interrompe :"))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    print('<<< VOLTE SEMPRE >>>')

