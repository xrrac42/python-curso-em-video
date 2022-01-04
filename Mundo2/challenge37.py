num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] BINARIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')
option= input("Sua opção: ")

if option == "1":
    base= 'BINARIO'
    resultado =bin(num)
elif option == "2":
    base = 'OCTAL'
    resultado = oct(num)
elif option == "3":
    base = 'HEXADECIMAL'
    resultado = hex(num)


print(f'{num} convertido para {base} é igual {resultado[2:]}')



