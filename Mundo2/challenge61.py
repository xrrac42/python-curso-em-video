print('=-'*20)
print('Gerador de Pa'.upper())
print('=-'*20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da sua PA: '))
termo = primeiro
cont= 1


while cont <=10:
    print(f'{termo}->',end= "")
    termo += razão
    cont+=1 

print('FIM')