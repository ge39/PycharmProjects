'''
    detector de palindromo, desconsoderando os espaços
    a sacada da casa
    o lobo ama o bolo
    a torre da derrota

'''
frase = str(input('Digite uma Frase :')).strip().upper()
palavras = frase.split()    # cria uma lista, e separa as palvras entre espaços
junto = ''.join(palavras)   # juntou a lista

# 1ª opção de solução
#inverso = ''
#   o laço for inverte a frase da ultima letra para a primeira
#  for letra in range(len(junto)-1, -1, -1):
    #  inverso += junto[letra]

# 2ª opção de solução
inverso = junto[::-1]
print(inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')