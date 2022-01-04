peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / altura**2

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa PESO NORMAL') 
elif 25 <= imc < 30:
    print('Você está em SOBREPESO') 
elif 30 <= imc <40:
    print('Você está em OBESIDADE, cuidado ') 
elif imc >= 40:
    print('Vocẽ está com OBESIDADE MÓRBIDA')         
