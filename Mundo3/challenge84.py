pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso em Kg: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    while True:
        parada = input('Deseja continuar?[S/N] ').upper()[0]
        if parada == 'N' or parada == 'S':
            break
        print('RESPOSTA INVÀLIDA!')

    if parada == 'N':
        break

print(f'Ao todo voce cadastrou {len(pessoas)} pessoas')

print(f'O maior peso cadastrado foi {maior:.2f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')

print(f'\nO menor peso cadastrado foi {menor:.2f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
print()