from random import randint
from time import sleep
lista = []
jogos = []
print('|' * 30)
print('Jogo da Mega-Sena'.center(30, '|'))
print('|' * 30)
print()
quant = int(input('Quantos jogos você quer que eu faça sorteio: '))

tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()    
print(f'Sorteando {quant} jogos'.center(30, '|'))
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l} ')
    sleep(2)
print('BOA SORTE!')    
