ficha = {}

ficha['nome'] = input('Digite o nome: ')
ficha['media'] = float(input(f'Media de {ficha["nome"].upper()}:'))

print(f'- NOME: {ficha["nome"].upper()}')
print(f'- A MEDIA: {ficha["media"]:.2f}')
if ficha['media'] >= 7: 
    print('- SITUAÇAO: APROVADO')
elif ficha['media'] >= 5:
    print('- SITUACAO: RECUPERACAO')   
elif ficha['media'] <5:
    print('- SITUAÇAO: REPROVADO')    

