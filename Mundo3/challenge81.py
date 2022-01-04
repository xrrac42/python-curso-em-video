valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        parada = input('Deseja continuar? ').upper()[0]
        if parada == 'N' or parada == 'S':
            break
        print('Resposta inválida!. Digite [S/N]')

    if parada == 'N':
        break

valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos')
print('Você digitou os seguintes valores ', end='')
for valor in valores:
    print(valor, end=' ')
contador5 = valores.count(5)
if contador5 >= 1:
    print('\nO valor 5 faz parte da lista')
else:
    print('\nO valor 5 não está na lista')

