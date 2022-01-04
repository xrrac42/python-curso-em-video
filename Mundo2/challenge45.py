storename = "LOJA DO CADU"

print(f'{storename:=^40}')

order = float(input('Preço da compra: '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro ou cheque ')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

escolha = int(input('Qual sua escolha: '))

if escolha == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = order + order * 0.20
    juros = valor / parcelas
    print(
        f'Sua compra será parcelada em {parcelas}x de R${juros:.2f} COM JUROS '
    )
    print(f'Sua compra de R${order:.2f} vai custar R${valor:.2f}, no final')
elif escolha == 3:
    double = order / 2
    print(f'Sua compra será parcelada em 2x de R${double:.2f}')
elif escolha == 2:
    desconto = order - order * 0.05
    print(f'Sua compra de R${order:.2f} vai custar R${desconto:.2f} no final')
elif escolha == 1:
    desconto = order - order * 0.1
    print(f'Sua compra de R${order:.2f} vai custar R${desconto:.2f} no final')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente')
