from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opção = 0

while opção !=5:
    print('---' * 20)
    print('''  
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa
 ''')
    print('---' * 20)
    opção = int(input('Qual sua opção? '))
    if opção == 1:
       soma = n1+n2
       print(f'A soma de {n1} + {n2} é {soma}')
    elif opção == 2:
        multiplica = n1 * n2
        print(f'{n1} x {n2} = {multiplica}')
    elif opção == 3:
        if n1 < n2:
            maior = n2
            menor = n1
        else:
            maior = n1
            menor = n2

        print(f'O maior é o número {round(maior)} e o menor múmero é o {round(menor)}')    
    elif opção == 4:
        n1 = int(input('Qual é o primeiro valor? '))
        n2 = int(input('Qual o segundo valor? '))    
    else:
        print('Dados inválidos. Tente novamente') 

print('Finalizando programa...')
sleep(4)
print('Fim do programa, Volte sempre')    


  





    