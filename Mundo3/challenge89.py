ficha = []


while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Nota 1 '))
    nota2 = float(input('Nota 2 '))
    media = (nota1 + nota2) /2
    parada = input('Deseja parar ').upper()
    ficha.append([nome, [nota1, nota2], media])
    if parada == 'S':
        break
    
for i,a in enumerate(ficha):
    print(f"{i:<4} {a[0]:<10} {a[2]:>4.1f} ")

while True:
    opcaoAluno = int(input('Digite o numero do aluno que deseja saber os dados: [999] para parar'))
    if opcaoAluno == 999:
        break
    if opcaoAluno <= len(ficha)-1:
        print(f'Notas de {ficha[opcaoAluno][0]} são {ficha[opcaoAluno][1]}')    


    
    


