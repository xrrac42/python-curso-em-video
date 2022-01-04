print('*'*30)
print('*'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('*'*30)
from random import randint
count = 0

while True:
    computador = randint(0, 11)
    print('*'*30)
    numero = int(input("Qual numero você quer? "))
    print('*'*30)
    condicao = str(input('Par ou Impar [P/I] ')).upper()
    print('*'*30)

    soma = numero + computador
    
    if soma % 2 == 0:
        resultado = 'P'
        resposta = 'DEU PAR'
    else:
        resultado = 'I'
        resposta = 'DEU IMPAR'
    print('*'*30)
    if resultado == condicao:
        print('VOCE VENCEU')
        print('Vamos jogar novamente...')
    else:
        break
    
    count = count + 1
print('*'*30)
if count == 0:
    print('Você venceu nehuma vez')
elif count == 1:
    print('Você venceu uma vez')
else:
    print(f'Você venceu {count} vezes')
print('GAME OVER')
print(
    f'Voce jogou {numero} e o computador {computador} a soma deu {soma}. {resposta}'
)
print('*'*30)