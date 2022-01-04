valores = []

while True:
    valor = int(input('Digite um valor para lista: '))
    if valor in valores:
        print('Já existe esse valor, não vou adicionar')
    else:
        valores.append(valor)
        print(f'O valor {valor} foi adicionado com sucesso')
    while True:
        parada = input('Deseja continuar? [S/N]').upper()
        if parada == 'N' or parada == 'S':
            break
        print('Digite uma opcao entre S ou N. S para sim e N para não')
    if parada == 'N':
        break
  

valores.sort()
print(f'Voce digitou os valores {valores}')
