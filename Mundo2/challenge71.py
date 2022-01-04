print('=' * 30)
print('{:^30}'.format('O BANCO'))
print('=' * 30)
valor = int(input('Digite o valor de saque R$: '))
total = valor
ced = 50
totalced = 0

while True:
    if ced >= 50:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
    

