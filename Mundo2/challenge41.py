from datetime import date

birthday = int(input('Ano de nascimento: '))
year = date.today().year
age = year - birthday

if age <= 9:
    categoria = 'mirim'
elif age <= 14:
    categoria = 'infantil'
elif age <=19:
    categoria = 'junior'
elif age <= 25:
    categoria = 'sênior'
elif age > 25:
    categoria = 'master'

print(f'O atleta tem {age} anos')
print(f'Classificação: {categoria.upper()}')

       
