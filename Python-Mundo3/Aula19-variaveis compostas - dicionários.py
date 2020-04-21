
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
print('.'* 100)
print('              0                  |              1                 |              2               |   ')