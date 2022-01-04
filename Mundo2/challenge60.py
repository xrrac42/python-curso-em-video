print("Digite um numero para")
numero = int(input('Para calcular seu fatorial: '))
fatorial = 1
count = numero
fatorial = 1
print(f'Calculando {numero}!')

while count > 0:
    print(count, end=' ')
    print('x ' if count > 1 else ' = ', end=' ')

    fatorial *= count
    count -= 1
 
print(fatorial, end='')
print()