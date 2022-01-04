cadastro = {}
gols = []
jogadores = []

while True:
    cadastro.clear()
    gols.clear()
    cadastro['nome'] = input('Nome do jogador: ')
    cadastro['partidas'] = int(input('Partidas jogadas: '))
    
    for x in range(1, cadastro['partidas'] + 1):
        gols.append(int(input(f'Quantos gols na partida {x} ')))
        cadastro['gols'] = gols[:]
    cadastro['total'] = sum(cadastro['gols'])

    while True:
        parada = input('Deseja continuar? [S/N]'.upper()).upper()
        if parada == 'N' or parada == 'S':
            break
    jogadores.append(cadastro.copy())
    if parada == 'N':
        break



print(jogadores)
print('Codigo',end=' ')
print('nome',end=' ')
print('partidas',end=' ')
print('gols', end='')
print()
for indice, dados in enumerate(jogadores):
    print(f"{indice:>1}{dados['nome']:>3}{dados['partidas']:>3}{sum(dados['gols']):>3}")

while True:
    escolha = int(input('Mostrar dados de qual Jogador? [999 para parar] '))
    if escolha == 999:
        break
    print(f'Levantamento jogador {jogadores[escolha]["nome"]}')
    for indice, informacoes in enumerate(jogadores[escolha]["gols"]):
        print (f'partida {indice+1} {informacoes} gols')    

