n = 0
r = 'S'

while r == 'S':
    n = int(input('Digite um numero :'))
    n += n
    r = str(input('Quer continuar ? S/N :')).upper().strip()
    print(n)
print('FIM')