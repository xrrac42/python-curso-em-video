total = maior = countmil = count = 0
barato = caro = ''

while True:
    produto = input('Digite o nome do produto: ')
    count += 1
    preco = float(input('Digite o valor do produto: '))
    parada = ' '
    while True:
        parada = input("Quer continuar [S/N]?").upper()
        if parada == 'S' or parada == 'N':
            break

    total += preco

    if preco >= 1000:
        countmil += 1

    if count == 1:
        maior = menor = preco
        barato = caro = produto
    else:
        if preco > maior:
            maior = preco
            caro = produto
        if preco < menor:
            menor = preco
            barato = produto

    if parada == 'N':
        break

print()
print('******RELATÓRIO DA COMPRAR*******')
print(f'O total da compra foi R${total:.2f}')
print(f'{countmil}  custam mais de R$1000.00')
print(f'O produto mais caro foi {caro} e custa R${maior:.2f}')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')