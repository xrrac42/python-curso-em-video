galera = []
pessoa = {}
somaIdade = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ').upper()[0]
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
        print('Erro! Digite apenas M ou F')
        
    pessoa['idade'] = int(input('IDADE: '))
    somaIdade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        parada = input('Deseja parar[S/N]').upper()[0]
        if parada == 'N' or parada == 'S':
            break
        print('Entrada inválida. Digite apenas S ou N')

    if parada == 'S':
        break

media = somaIdade / len(galera)    
print(f'Ao total foram cadastradas {len(galera)} pessoas ')
print(len(galera))

print(f'A média de idade é {media:5.2f} anos')

print('As mulheres cadastradas foram: ',end='')
for mulher in galera:
    if mulher['sexo'] == 'F':
        print(mulher['nome'], end='')
print()
print('Pessoas acima da média' , end='')
for individuo in galera:
    if individuo['idade'] >= media:
        print(f"{individuo['nome']}, {individuo['idade']} anos", end=' ')
