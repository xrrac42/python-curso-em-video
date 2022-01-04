print('=-' * 20)
print('Gerador de Pa'.upper())
print('=-' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da sua PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}->', end="")
        termo += razão
        cont += 1
   
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} de termos')    
print('FIM')