from random import randint
from time import sleep
from operator import itemgetter


jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
raking = {}
print('Valores sorteados')
for jogador, jogada in jogo.items():
    print(f'{jogador} tirou {jogada} no dado')
   
print('|'*40)
raking = sorted(jogo.items(), key= itemgetter(1), reverse= True)

for indice,valores in enumerate(raking):
    print(f'{indice+1}º {valores[0]} com {valores[1]}')