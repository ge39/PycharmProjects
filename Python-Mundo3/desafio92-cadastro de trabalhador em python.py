'''
Crie um programa que leia: nome, ano de nascimento e carteira de trabalho e cadsastre-os com (idade)
em um dicionario se por acaso a ctps for diferente de zero, o dicionario receberá tambem o ano de contratação
e o salario.Calcule e acrescente, alem, da idade, com quantos anos a pessoa vai se aposentar
'''
from datetime import date
ficha = dict()
ano_atual = date.today().year
ficha['nome'] = str(input('Nome:').upper())
nascido=int(input('Nascido em: '))
ficha['idade'] = ano_atual - nascido
ficha['ctps'] = int(input('Carteira Prof [0] nao possui: '))
if ficha['ctps'] != 0:
  ficha['contrato'] = int(input('Ano Contrato: '))
  ficha['salario'] = float(input('Salário: R$'))
  ficha['aposentadoria'] = ficha['contrato'] + 35
for k, v in ficha.items():
    print(f'- {k} tem o valor {v}')