from datetime import date

ano= int(input('Digite o ano que deseja? Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year

if ano%4== 0 and ano%100 !=0 or ano%400== 0:
    resultado="bissexto"
else:
    resultado="não é bissexto"

print(f'O ano de {ano} {resultado}')
