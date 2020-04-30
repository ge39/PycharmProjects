'''
Crie um programa que leia: nome, ano de nascimento e carteira de trabalho e cadsastre-os com (idade)
em um dicionario se por acaso a ctps for diferente de zero, o dicionario receberá tambem o ano de contratação
e o salario.Calcule e acrescente, alem, da idade, com quantos anos a pessoa vai se aposentar
'''
from datetime import date
dados = dict()
ano_atual = date.today().year
dados['nome'] = str(input('Nome: ').upper())
nascido=int(input('Nascido em: '))
dados['idade'] = ano_atual - nascido
dados['ctps'] = int(input('Carteira Prof [0] nao possui: '))

if dados['ctps'] != 0:
  dados['contrato'] = int(input('Ano Contrato: '))
  dados['salario'] = float(input('Salário: R$ '))
  dados['aposentadoria'] = dados['idade'] + ((dados['contrato'] + 35) - ano_atual)

for k, v in dados.items():
    print(f'- {k} tem o valor \033[34m{v}\033[m')