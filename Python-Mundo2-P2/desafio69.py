'''
    CRIE UM PROGRAMA que leia a idade e sexo de várias pessoas
    a cada pessoa cadastrada, o programa deverá perguntar seo usuario quer ou nao continuar
    no final mostre.
    A - quantas pessoas com mais de 18 anos
    B - quantos homens foram cadastrados
    C - quantas mulheres tem menos de 20 anos
'''

iniciar = 'S'
continuar = 'S'
idade = contsexo = fem = masc = 0
sexo = 'F'
while continuar in 'sS':
    idade = int(input('Qual é a sua idade: ?'))
    sexo = str(input('Informe o sexo [M] Masculino, [F] Feminino :')[0]).upper()
    continuar = str(input('\033[32mDeseja continuar cadastrando: ?\033[m')).upper()
    contsexo += 1
    print('*' * 60)

    if idade > 18:
        contsexo
    if sexo == 'M':
         masc += 1
    if idade < 20 and sexo == 'F':
        fem += 1
else:
    print(f'Temos {contsexo} pessoas com mais de 18 anos')
    print(f'Total de {masc} pessoas do sexo masculino')
    print(f'Total de {fem} pessoas do sexo feminino com menos de 20  anos')
