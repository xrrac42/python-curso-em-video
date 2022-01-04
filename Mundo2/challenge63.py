print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos você quer mostrar = '))
t1 = 0
t2 = 1
print(t1, end='->')
print(t2, end='->')
count = 0
while True:
    t3 = t1 + t2
    print(t3, end='->')
    t1 = t2
    t2 = t3

    count = count + 1

    if count == n:
        break

print('fim', end='')
print()
