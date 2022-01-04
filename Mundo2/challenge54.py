from datetime import date

atual = date.today().year
countMaior = 0
countMenor = 0
print()
print("ANALISADOR DE MAIOR IDADE")
print()
for x in range(1, 7 + 1):
    ano = int(input(f'Em que ano a {x}ª pessoa nasceu? '))
    if atual - ano >= 18:
        countMaior += 1
    else:
        countMenor += 1

print()
print(f"Ao todo tivemos {countMaior} pessoas maiores de idade")
print(f"E também {countMenor} pessoas menores de idade")
