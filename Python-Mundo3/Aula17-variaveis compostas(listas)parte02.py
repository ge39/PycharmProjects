''''
Variaveis compostas (listas) - MUTAVEL
Listas dentro de lista
'''

dados = []
dados.append('Pedro')
dados.append(25)
print(f' {dados}')
print("\033[34mPodemos exibir os dados usando seu index\033[m")

print("  \033[33mExibindo o dado de toda a lista usando o [:] como index \033[m")
print(f'  {dados[:]}')
print("  \033[33mExibindo o dado do index [0]\033[m")
print(f'  {dados[0]}')
print("  \033[33mExibindo o dado do index [1]\033[m")
print(f'  dados[1]')
print("")

print("\033[34mDeclarando uma outra estrutura chamada 'Pessoa'\033[m")
pessoa = []

print("  \033[33mCopiando a estrutura da lista dados para a estrutura Pessoa (dados[:])\033[m")
pessoa.append(dados[:])
print(f'  {pessoa}')
print("")
print("  \033[33mCriando uma lista composta de dados para a estrutura lista Pessoa \033[m")
pessoa = [['Pedro', 25], ['Maria', 19], ['João', 22]]
print(f'  {pessoa}')
print("")
print("  \033[33mListando os dados da estrutura lista Pessoa, usando o index pessoa[0][0]\033[m")
print(f'  {pessoa[0][0]}')
print("")
print("  \033[33mListando os dados da estrutura lista Pessoa, usando o index pessoa[0][1]\033[m")
print(f'  {pessoa[0][1]}')
print("")
print("  \033[33mListando os dados da estrutura lista Pessoa, usando o index pessoa[0],\n  trazendo todos os dados do index 0 da lista Pessoa\033[m")
print(f'  {pessoa[0]}')
print("")
print("  \033[33mListando os dados da estrutura lista Pessoa, usando o index pessoa[1][:],\n  trazendo todos os dados do index 1 da lista Pessoa\033[m")
print(f'  {pessoa[1][:]}')
print("")
print("  \033[33mListando todos os dados da estrutura lista Pessoa \n  trazendo todos os dados não definindo o index\033[m")
print(f'  {pessoa}')

