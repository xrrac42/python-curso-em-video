valores = (
    int(input('Valor 1: ')), int(input('valor 2: ' )), int(input('Valor 3: ')),
    int(input('valor 4: '))
)
count9 = 0
count3 = 0
countPar = 0

print(f'Os valores digitados foram {valores}')

for numero in valores:
    if numero == 9:
        count9 += 1
if count9 >= 1:
    print(f'O numero 9 foi digitados {count9} vezes')
else:
    print(f'Não ha nenhuma ocorrecia do numero 9')       
for numero in valores:
    if numero == 3:
        count3 += 1
if count3 >= 1:
    print(f'O primeioro 3 aparece na posição {valores.index(3)+1}')
else:
    print('Não há nenhum três na sequencia digitada')    

for numero in valores:
    if numero %2 == 0:
        countPar += 1   
if countPar>= 1:
    print(f'Foram digitados {countPar} numeros pares')
else:
    print(f'Não foi digitado nenhum numero par')     
             

