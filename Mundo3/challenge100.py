import tqdm
from random import randint
from time import sleep





def sorteia():

    print('Sorteando 5 valores')
    for cont in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)

        print(f'{n}', end=' ', flush=True)
        sleep(0.2)
    for i in tqdm(range(100), desc='Loading...', ascii = False, ncols= 75):
        time.sleep(0.10)
        print('Loadin done...')

def somaPar():
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)


numeros = list()
pares = []
sorteia()
somaPar()
print(f'\nSoma dos pares em {numeros} é igual a {sum(pares)}')