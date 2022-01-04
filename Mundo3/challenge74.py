from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print('Os valoes sorteados foram', end=' ')
for n in numeros:
    print(n, end=' ')

print()
print(f'O maior numero sorteado foi {max(numeros)} e o menor numero foi {min(numeros)}')
