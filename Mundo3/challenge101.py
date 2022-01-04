from datetime import date
year_today = date.today().year
def voto(year):
    if year_today - year >= 16:
        saida = 'VOTO OBRIGATÒRIO'

    if year_today - year < 16:
        saida = 'NÃO PODE VOTAR'

    if year_today - year >= 65:
        saida = 'OPCIONAL'

    return saida


print('Programa que informa a obrigatorieadade do voto'.upper())

year = int(input('Em qual ano você nasceu: '))

print(f'Com {year_today-year} anos: {voto(year)}')
