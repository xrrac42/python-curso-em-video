salario= float(input('Qual o valor do salário do funcionário? R$'))
ajust= salario+ (salario*15/100)
print(f"Um funcionário que ganhava R${salario:.2f}, com aumento de 15%, passa a receber R${ajust:.2f}")