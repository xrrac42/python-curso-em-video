from random import randint
from time import sleep

print('-=-'*25)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar!'.upper())
print('-=-'*25)
num = int(input('Em que numero pensei? '))
numberSelect = randint(0, 5)
print('Processando...')
sleep(2)

if numberSelect == num:
    print(f"Parabens, vc ganhou! Eu pensei no numero {numberSelect}")
else:
    print(f"Voce perdeu! Eu pensei no número {numberSelect}")

# print(f'O numero que eu computador escolhi foi {numberSelect} e o número que vc escolheu foi {num}')