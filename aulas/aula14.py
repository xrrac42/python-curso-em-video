# for c in range(1,11):
#     print(c)
# print('fim')    

# c = 1

# while c <11:
#     print(c)
#     c = c +1
# n = 1
# r = 'S'

# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar?')).upper()
# print('Stop it')    
n=1
count = 0
par = impar = 0
while n != 0:
   n= int(input('Digite um numero: '))
   if n !=0:
        if n %2 == 0:
            par += 1
        else:
            impar +=1
       
   count = count + n

print(f'Foram digitados {impar} numeros impares ')
print(par)
print(count)
