primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao= int(input('Digite a razão: '))
decimo = primeiroTermo + (10-1) * razao

for c in range(primeiroTermo,decimo,razao):
    print(f'{c}',end= '->' )
print('finish')    