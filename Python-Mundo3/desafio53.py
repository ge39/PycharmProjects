#  crie um programa que leia uma frase qualquer e diga se ele é um palindromo,
#  desconsiderando os espacos

frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()    #divide a frase
junto = ''.join(palavras)   # remove os espaços entre as palavras e as une
inverso = junto[::-1]

'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

print('A frase escrita {}, {} '.format(inverso, junto))
if inverso == junto:
    print('Essa frase é um Palíndromo')
else:
    print('Essa frase não é um Palindromo')