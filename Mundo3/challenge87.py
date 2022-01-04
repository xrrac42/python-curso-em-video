matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite o numero da linha {linha}e da coluna{coluna}: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'|{matriz[linha][coluna]}|', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapares = somapares + matriz[linha][coluna]

    print()

print(f'A soma dos pares é {somapares}')
print(sum(f'A soma da terceira linha é {matriz[2]}'))
print(max(f'O maior numero da segunda linha foi {matriz[1]}'))
