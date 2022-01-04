cadastro = {}
gols = []
cadastro['nome'] = input('Nome do jogador: ')
cadastro['partidas'] = int(input('Partidas jogadas: '))

for x in range(1, cadastro['partidas'] + 1):
    gols.append(int(input(f'Quantos gols na partida {x} ')))
    cadastro['gols'] = gols[:]
cadastro['total'] = sum(cadastro['gols'])

print('=-' * 40)
print(cadastro)
print('=-' * 40)
print(f"NOME: {cadastro['nome']}")
print(f"GOLS: {cadastro['gols']}")
print(f"TOTAL DE GOLS: {cadastro['total']}")
print('=-' * 40)
print(f"O jogador {cadastro['nome']} jogou {cadastro['partidas']} partidas")
for partidas, gols in enumerate(cadastro['gols']):
    print(f'=> Na partida {partidas+1} foram marcados {gols} gols')
print(f"Foi um total de {cadastro['total']} gols")
