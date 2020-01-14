c1 = c2 = c3 =  0
for c in range(1, 101):
    if c % 3 == 0:
      c = 'Fizz'
    elif c % 5 == 0:
       c = 'Buzz'
    elif c % 3 == c % 5:
        c = 'Fizz Buzz'
    print(f'{c}')
