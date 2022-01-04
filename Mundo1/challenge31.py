km = float(input('Qual a distancia da sua viagem? '))

print(f'Você está preste a viajar {km} km')

if km <= 200:
    price = km*0.50
else:
    price = km*0.45

print(f'É o preço da sua passagem será R${price:.2f}')
