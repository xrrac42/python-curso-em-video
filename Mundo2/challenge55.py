maior = 0
menor = 0
n = 4
for p in range(1,n):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso foi de {menor}kg')          
                 
