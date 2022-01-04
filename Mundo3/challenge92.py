ficha = {}
from datetime import date
ano = date.today().year

ficha['nome'] = input('Nome: ')
ficha['nascimento'] = int(input('Ano de nascimento: '))
ficha['ctps'] = int(input('Carteira de Trabalho. Se não tiver digite (0): '))

if ficha['ctps'] != 0:

    idade = ano - ficha['nascimento']
    ficha['admissao'] = int(input('Ano de cotratação: '))
    ficha['salario'] = float(input('Salario: '))
    ficha['idade'] = idade
    ficha['aposentadoria'] = ficha['admissao'] + 35 - ficha['nascimento']

if ficha['ctps'] == 0:
    idade = ano - ficha['nascimento']
    ficha['idade'] = idade
    print('FICHA TRABALHADOR')
    print(f"NOME: {ficha['nome']}")
    print(f"IDADE: {ficha['idade']}")
    print(f"CTPS: {ficha['ctps']}")

if ficha['ctps'] > 0:
    print('FICHA TRABALHADOR')
    print(f"NOME: {ficha['nome']}")
    print(f"CTPS: {ficha['ctps']}")
    print(f"CONTRAÇÃO: {ficha['admissao']}")
    print(f"IDADE: {ficha['idade']}")
    print(f"SALARIO: {ficha['salario']}")
    print(f"APOSENTADORIA: {ficha['aposentadoria']} anos")
