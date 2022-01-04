from time import sleep

def contador(inicio,fim,passo):
    print(f'\ncontagem de {inicio} até {fim} em {passo}')
  
    if inicio < fim:
        for c in range(inicio,fim+1, passo):
            print(c,end=',', flush = True)
            sleep(0.5)
    else:
        for c in range(inicio,fim+1,-passo):
            print(f'{c}',end=',', flush = True)
            sleep(0.5)

contador(10,1,1)
contador(2,10,2)
print('Agora é sua vez')
inicio = int(input('Digite o inicio da contagem: '))
fim= int(input('Digite o fim da contagem: '))
passo = int(input('Digite o passo da contagem:'))
contador(inicio,fim,passo)

