from datetime import date
birthday = int(input('Ano de nascimento: '))
year = date.today().year
age = year - birthday
enlistment = birthday + 18

if year - birthday == 18:
    print(f'Quem nasceu em {birthday} completa {age} anos em {year}')
    print('Você tem que se alistar IMEDIATAMENTE!')
elif year - birthday > 18:
    print(f'Quem nasceu em {birthday} tem {age} anos em {year}')
    print(f'Vocẽ deveria ter se alistado há {year- (birthday+18)} anos atrás')
    print(f'Seu alistamento foi em {enlistment}')
else:
    print(f'Quem nasceu em {birthday} tem {age} anos em {year}')
    print(f'Ainda faltam {enlistment - year} anos para seu alistamento')
    print(f'Seu alistamento será em {enlistment}')