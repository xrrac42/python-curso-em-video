count = 0
num = int(input('Digite um numero para descobrir se é primo '))

for c in range(1,num+1):
    if num % c == 0:
        count += 1

if count == 2:
    print(f'O numero {num} é PRIMO')
elif count >2:
    print(f"O numero {num} NAO É PRIMO")    