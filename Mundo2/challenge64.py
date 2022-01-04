soma = count = 0

while True:
    parada = int(input('Digite 999 para parar: '))
    if parada == 999:
        break

    count += 1
    soma = parada + soma

print(f'Você digitou {count} numeros e a soma entre eles foi {soma} ')
