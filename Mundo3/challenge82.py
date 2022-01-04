num = []
pares = []
impares = []

while True:
    num.append(int(input("Digie um valor")))
    while True:
        parada = input('Deseja continuar? [S/N] ').upper()
        if parada == 'N' or parada == 'S':
            break
    if parada == 'N':
        break
num.sort()    
for v in num:
    if v %2 == 0:
        pares.append(v)
for v in num:
    if v %2 == 1:
        impares.append(v)

print(f'os numeros digitados na lista fora {num}')
print(f'Os numeros pares digitados foram {pares}')
print(f'Os numeros impares digitados foram {impares}')