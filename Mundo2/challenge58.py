from random import randint
sorteio = randint(1,25)
contadorPalpites = 1

print(sorteio)
print("JOGO DA ADIVINHAÇÃO")
print()
print('Sou seu computador...')
print()
print('Acabei de pensar em um número entre 1 e 25. Você consegue adivinhar?')

palpite = int(input('Qual seu palpite? '))

while palpite != sorteio:
    if palpite > sorteio:
        palpite = int(input('Menos... Digite novamente: '))
    elif palpite < sorteio:
        palpite = int(input('Mais... Digite novamente: '))
    contadorPalpites += 1    
           

if contadorPalpites >1:
    print(f'Parabéns o número do sorteio é o {sorteio}, foram necessárias {contadorPalpites} tentativas')
else:
    print(f'Parabéns você acertou de primeira, ta usando hacker. O numero do sorteio foi {sorteio}')