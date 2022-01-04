casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario '))
anos = int(input('Em quantos anos deseja pagar? '))

prestaçoes = casa / (anos*12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos}. A prestação será de R${prestaçoes:.2f}')


if prestaçoes <= salario * 0.3:
    print('Empréstimo aprovado'.upper())
else:
    print('Empréstimo negado'.upper())



