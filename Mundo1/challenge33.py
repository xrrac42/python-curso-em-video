a= int(input('Digite o primeiro valor '))
b = int(input('Digite seu segundo valor '))
c= int(input('Digite o terceiro valor '))

menor = a
if b<c and b<a:
    menor =b
if c<a and c<b:
    menor= c

maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')    
