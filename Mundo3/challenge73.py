print('Campeonato Brasileiro série A'.upper())
tabela = ('Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza', 'Bahia',
          'Santos', 'Atlético Goianiense', 'Atlético Mineiro', 'Fluminense',
          'Flamengo', 'Corinthians', 'Ceará', 'Internacional', 'Juventude',
          'Sport', 'Cuiabá', 'São Paulo', 'Chapecoense', 'América',
          'Grêmio')

countPositionUp = 0

while True:
    timecoracao = input('Seu time do coração: ').title().strip()
    if timecoracao in tabela:
        break
    print(f'O time {timecoracao} não está na tabela. Digite um time da série A do Brasileirão  2021')

while True:
    print('ESCOLHA UMA DAS OPÇÕES: ')
    print()
    print('a) Os 5 primeiros times.')
    print('b) Os últimos 4 colocados.')
    print('c) Times em ordem alfabética.')
    print('d) Em que posição está seu time do coração.')
    print()
    while True:
        escolha = input('QUAL SUA ESCOLHA? ').upper().strip()
        if escolha in 'ABCD':
            break
        print('Digite uma opção válida!')
    
    if escolha == "A":
        print('Os primeiros 5 colocados são: ')
        for time in tabela[0:5]:
            countPositionUp += 1
            print(f'{countPositionUp}º {time}')

    if escolha == "B":
        print('Os quatro ultimos colocados são: ')
        for cont in range(16, len(tabela)):
            print(f'{cont + 1}º {tabela[cont]}')

    if escolha == "C":
        for time in sorted(tabela):
            print(time, end=' ')
    print()

    if escolha == "D":
        print(f'O time {timecoracao} esta na {tabela.index(timecoracao)+1}ª colocação do Brasileirao série A')

    parada = input('Deseja fazer uma nova conulta?' ).upper()

    if parada == "N":
        break


        





