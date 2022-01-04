countMulher20 = 0
countPessoas18 = 0
countHomens = 0
while True:
    print('*'*20)
    print('Cadaste uma pessoa:')
    print('*'*20)
    idade = int(input('Qual sua idade? '))
    print('*'*20)
    sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
    print('*'*20)

    if idade <= 18:
        countPessoas18 +=1

    if sexo == 'M':
        countHomens += 1
    if sexo == 'F' and idade < 20:
        countMulher20 = countMulher20 + 1
    
    parada = str(input('Quer continuar?[S/N] ')).upper()
    if parada == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {countPessoas18}') 
print(f'Total de homens cadastrados: {countHomens}')   
print(f'Total de mulheres com menos de 20 anos: {countMulher20}')
  