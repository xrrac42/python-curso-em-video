from time import sleep

def maior(*num):
  count = maior  = 0
  print('\nAnalisando os valores passados')    
  for numeros in num:
    print(f' {numeros}', end= ' ', flush = True)
    sleep(0.5)
    if count == 0:
      maior = numeros
    else:
      if numeros > maior:
        maior = numeros
    count += 1
  print(f'\n O maior valor foi {maior}')

maior(7,6,4,2,78)