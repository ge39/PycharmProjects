#  desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  no final, mostre os 10 primeiros termos dessa progressão.

print('\033[34m==\033[m'*20)
print('Progressão Aritmética')
primeiro = int(input('Primeiro termo :'))
razao = int(input('Razao :'))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end =' - ')
print('\nAcabou')
print('\033[34m==\033[m'*20)