sexo = str(input("Informe seu sexo? ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input('Dados inválidos, informe novamente seu sexo: '))

print(f'Sexo {sexo} registrado com sucesso')
