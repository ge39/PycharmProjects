
print('\033[31mEstrutura composta - Dicionário\033[m\nTuplas      ()\nListas      []\nDicionarios {}')

print('.' * 16)
print('|  Pedro  | 25 |')
print('.'* 16)

print('\033[31mDefinindo um dicionario, uma das formas é declarando dict()\033[m')
print('dados = dict ()\ndados = "{nome: Pedro,idade: 25}"')
dados = dict()
dados = {'nome': 'Pedro','idade': 25}
print(f'\033[34mO retorno é {dados}\033[m')
print('.'*60)
print('Quando trabalhamos com "listas()" os indices de cada elemento é representado numericamente 0, 1, 2,.....\n'
      'Agora que estamos estudando \033[34mDicionario\033[m, os indices de cada elemento poderá ser representados\n'
      'por um nome literal.\n'
      'Em nosso exemplo abaixo diremos que:\n'
      'dados é um dicionario\n'
      'nome - é o identificar de indice do nome Pedro')
print("\033[34mdados = 'nome : Pedro', 'idade: 25\033[m'\n"
      "e idade tambem é o identificador de indice do valor idade\n"
      "para exibir esses dados faremos :\n\033[34m"
      "print(dados['nome'])\033[m  = Pedro e \n\033[34mprint(dados['idade'])\033[m = 25")
print('.' * 16)
print('|  Pedro  | 25 |')
print('.'* 16)
print("\033[31mFinalizando :\033[m dados é a minha estrutura, 'Pedro' e '25' são meus elementos,\n"
      "'nome' e 'idade' são meus indices literais.")
print()
print("\033[34minserindo um novo elemento ao dicionario\033[m\n"
      "vamos inserir o elemento sexo a estrutura de dados de Pedro :\n"
      "sua sintase é : Estrutura, indice e elemento = dados['sexo']='M'")
print('.' * 22)
print('| \033[34m Pedro\033[m  | \033[34m25\033[m |  \033[33m M\033[m  |')
print('.'* 22)
print()
print('\033[34mRemovendo um elemento\033[m, usando o comando del\nO elemento que for selecionado dentro da estrutura de dados, o mesmo será removido, perdendo seu valor')
print("Ex: \033[34mdel\033[mdados\033[33m['idade']\033[m")
print('O elemento idade foi removido da minha estrutra DADOS')
print('.' * 18)
print('| \033[34m Pedro\033[m  |  \033[33m M\033[m  |')
print('.'* 18)
print()
print('OUTRO EXEMPLO DE DICONARIO PARA GUARDAR FILMES')
print('    titulo      ano       diretor')
print('.' * 40)
print('| \033[31m Star wars\033[m  | \033[31m1977\033[m |  \033[31m George Lucas\033[m  |')
print('.' * 40)
print("filme = \033[33m{\033[34m'titulo'\033[m: \033[31m'Star Wars'\033[m,"
      "\n          \033[34m'ano'\033[m: \033[31m1977,"
      "\n          \033[34m\033[34m'diretor'\033[m: \033[31m'George Lucas'\033[m"
      "\n        \033[33m}\033[m")
print('.'*40)
print("Podemos acessar os valores da estrutra filme\nutilizamos o método "
      "\033[33mvalues = \033[34mprint(\033[mfilme\033[31m.values()\033[34m)\033[m\n"
      "Ele retorna todos os elementos, 'Valores' do meu dicionario,'\033[34mStar Wars, 1977 e George Lucas\033[m'")
print()
print("Podemos acessar os indices da estrutra filme\nutilizamos o método "
      "\033[33mKey = \033[34mprint(\033[mfilme\033[31m.keys()\033[34m)\033[m\n"
      "Ele retorna todos os indices literais da estrutura,'\033[34mtitulo, ano e diretor\033[m' ")

print()
print("Podemos acessar os Keys(indices), Values(elementos) da estrutra filme\nutilizamos o método "
      "\033[33mitems = \033[34mprint(\033[mfilme\033[31m.items()\033[34m)\033[m\n"
      "Ele retorna todos os indices literais da estrutura,"
      "'\033[34mtitulo:Star Wars, ano:1977 e diretor:George Lucas\033[m' ")

print("Podemos trabalhar com tuplas, listas e dicionarios juntos, por exemplo :")
print()
print('Locadora' )
print('.'* 100)
print('.' * 97)
print(".|\033[34mStar wars|1977|'George Lucas'\033[m|**|'\033[33mAvengers'|2012|'Joss Whedon\033[m'|**|'\033[31mMatrix'|1999|'Wachowski\033[m'| .")
print('.' * 97)
print('  titulo     ano    diretor    |  |  titulo    ano     diretor  |  | titulo   ano    diretor')
print('.' * 100)
print('\033[31m               0                 |               1                |            2               |   \033[m')
print('No exemplo acima, Temos uma estrutura de lista \033[34mchamada locadora'
      '\033[m com 3 elementos,\033[31m 0, 1, 2\033[m\nDentro do elemento 0 temos: um dicionario, Elemento 1: um dicionario\n'
      'Elemento 2 outro dicionario\nAs listas são identificadas ou numeros '
      'e os dicionarios por textos (Chaves literais) e numeros ')
print()
print("\033[34mprint(\033[mlocadora\033[32m[0]['ano']\033[m\033[33m)\033[m\n"
      "Locadora = é o nome da minha estrutura, a lista\n"
      "\033[32m[0]\033[m = é a referencia externa, é o elemento que identifica o dicionario na lista\n"
      "\033[32m['ano']\033[m = é a chave do meu dicionario que está no elemento zero")
print("Exemplificando :\n\033[34mprint(\033[mlocadora\033[32m[0]['ano']\033[m\033[33m)\033[m = 1977")
print("\033[34mprint(\033[mlocadora\033[32m[2]['titulo']\033[m\033[33m)\033[m = Matrix")
print()
print('-=' * 70)
print('Exercicios na prática')
print('-=' * 70)
pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 40}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('Exibindo os valores das \033[31mkeys\033[m "indices')
print(pessoas.keys())
print()
print('Exibindo os valores com \033[31mValues\033[m "elementos"')
print(pessoas.values())
print()
print('Exibindo os valores das \033[31mitems\033[m " chave valor ou indices e elementos')
print(pessoas.items())
print()
print('usando um laço for para acessar entre as keys ')
print()
pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 40}
print('Exibe apenas os valores das keys "indices"', end=" ")
for k in pessoas.keys():
      print(f'\033[34m{k}, \033[m', end="")
print()
print('usando um laço for para acessar entre as values')
print()
print('Exibe apenas o conteudo dos Values "elementos', end =" ")
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 40}
for v in pessoas.values():
      print(f'\033[34m{v}, \033[m', end="")
print()
print('Usando o items, "chave , Valor = indice, elemento"')
for k, v in pessoas.items():
      print(f'chave \033[34m{k} = {v}, \033[m')
print()
print("apagando um elemento, o elemento Sexo será eliminado, com o comando del pessoas['sexo'']")
del pessoas['sexo']
for k, v in pessoas.items():
      print(f'{k} = {v}')
print()
print("Substituindo o nome Gustavo por Leandro, com o comando pessoas['nome'] = 'Leandro']")
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 40}
pessoas['nome'] = 'leandro'
for k, v in pessoas.items():
      print(f'{k} = {v}')
print()
print("Adicionando um elemento na lista pessoas, pessoas['peso'] = 98.7")
pessoas['peso'] = 98.7
for k, v in pessoas.items():
      print(f'{k} = {v}')
      print()
print('\033[46mCriando um Dicionário dentro de uma lista\033[m')
print("brasil = [] - Lista\nestado1 = {'uf': 'Rio de Janeiro'} - dicionario\n"
      "estado2 = {'uf': 'Sao Paulo'} - dicionario")


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'Sao Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print("\033[46mInserindo o dicionario dentro da lista utilizando o metodo append:\033[m\n"
      "brasil.append(estado1)\nbrasil.append(estado2)")
print()
print("\033[46mExibindo o dicionario:\033[m estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}\n")
print(f'{brasil} - "print(brasil)"')
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print()
print("\033[46mExibindo o dicionario:\033[m estado2 = {'uf': 'Sao Paulo','sigla':'SP'}\n")

print(brasil[1])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])

print('\033[46mUtilizando o métoo append em dicionarios\033[m -  brasil.append(estado.copy())')
estado = dict()
brasil = list()

for c in range(0, 3):
      estado['uf'] = str(input('Unidade da Federação :')).upper()
      estado['sigla'] = str(input('Sigla do estado: ')).upper()
      brasil.append(estado.copy())
      print('Utilizando os metodos chaves e valores ')
for e in brasil:
      #print(e)

   #for k, v in e.items():
       #(f'O campo {k} tem o valor de \033[34m{v}\033[m')

   for v in e.values():
        print(v,end=' ')
   print()