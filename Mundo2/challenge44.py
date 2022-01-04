from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

nome = input('Qual seu nome?')

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('=-'*20)
print(f'Computador jogou {(itens[computador])}')
print(f'{nome} jogou {itens[jogada]}')
print('=-'*20)

if computador == 0: #PEDRA
        if jogada == 0:
                print('empate')
        elif jogada == 1: #PAPEL
                print('Você venceu')
        elif jogada == 2:#PRINT
                print('Você perdeu')
        else:
            print('Jogada inválida')        
            

elif computador == 1: #PAPEL
        if jogada == 0: #PEDRA
                print('Você perdeu')        
        elif jogada == 1: #PAPEL
                print('empate')

        elif jogada == 2:  #TESOURA  
                print('Você ganhou')
elif computador == 2:
        if jogada == 0:
                print('jogada vence')
        elif jogada == 1:
                print('Você perdeu')
        elif jogada == 2:
                print('Empate')

