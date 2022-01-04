salario = float(input('Qual o valor do salário do funcionário? '))

if salario <= 1250:
    ajuste = salario + salario*0.15
else:
    ajuste = salario + salario *0.10

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${ajuste:.2f} agora')        