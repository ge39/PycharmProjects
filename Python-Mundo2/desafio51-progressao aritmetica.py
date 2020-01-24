'''
    progressão aritmetica
'''
print('='*30)
print('10 TERMOS DE UMA PA' )
print('='*30)

primeiro = int(input('Primeiro termo :'))
razao = int(input('Razao :'))
progressao = int(input('Progressao :'))
decimo = primeiro + (progressao) * razao
continuar = 'N'


for pa in range(primeiro, decimo, razao):
    print(f'{pa}', end=' -> ')


