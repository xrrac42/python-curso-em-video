sequencia = ('zero', 'um', 'dois', 'três', 'quatro',
             'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
             'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
             'dezenove', 'vinte')

while True:
    escolha = int(input('De 0 a 20. Digite um número para obter ele por extenso: '))
    if escolha <= 20:
        break
    print('Digite um numero válido')

print(sequencia[escolha])    




