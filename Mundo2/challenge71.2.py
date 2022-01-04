print('=' * 30)
print('{:^30}'.format('CADUUUU BANK'))
print('=' * 30)
valor = int(input('Digite o valor de saque R$: '))

n50 = valor // 50
c20 = valor % 50
n20 = c20 // 20
c10 = c20 % 20
n10 = c10 // 10
c1 = c10 % 10
n1 = c1

lista1 = [
    f'{n50} NOTAS DE 50 REAIS', f'{n20} NOTAS DE 20 REAIS',
    f'{n10 } NOTAS DE 10 REAIS', f'{n1} NOTAS DE 1 REAL'
]

lista = [n50, n20, n10, n1]

for c in range(0, 4):

    if valor < 0:

        print('Impossivél')

        break

    if lista[c] > 0:

        print(lista1[c])