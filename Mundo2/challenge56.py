somaIdade = 0
mediaIdade = 0
maiorIdadeHomen = 0
nomeVelho = ""
totMulher20 = 0

for p in range(1, 5):
    print(f'{p}ª PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in "Mm":
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in "Mm" and idade > maiorIdadeHomen:
        maiorIdadeHomen = idade
        nomeVelho = nome
    if sexo in "fF" and idade <20:
        totMulher20 += 1

mediaIdade = somaIdade / 4
print(f'A média de idade desse grupo é de {mediaIdade} anos')
print(f"O homem mais velho tem {maiorIdadeHomen} e se chama {nomeVelho}")
print(f"Ao todos são {totMulher20} mulheres com menos de 20 anos")
