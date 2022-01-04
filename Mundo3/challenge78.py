valores = []

for valor in range(0, 5):
    valores.append(int(input(f'Digite o valor da posicao {valor} ')))


maior = max(valores)
menor = min(valores)

print(f'O maior valor foi {maior} e aparecem nas posicoes ', end='')
for pos, x in enumerate(valores):
    if x == maior:
        print(f'{pos}...', end=' ')


print(f'\nO menor valor digitado foi {menor} e aparecem na posicoes ',end=' ')
for pos, x in enumerate(valores):
    if x == menor:
        print(f'{pos}...', end=' ')     
