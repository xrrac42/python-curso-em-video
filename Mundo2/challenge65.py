maior = menor = soma = count = 0

while True:
    num = int(input('Digite um numero qualquer: '))
    condicao = str(input('Quer continuar? [S/N] ').upper())
    soma += num
    count += 1

    if count == 1:
        menor = maior = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    if condicao == "N":
        break

media = soma / count

print(f'Você digitou {count} números e a média foi {media:.1f}')
print(f'O maior valor foi {maior} e menor valor foi {menor}')

