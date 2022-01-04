velocidade = float(input("Digite a velocidade atual do seu carro "))
multa= (velocidade -80)*7

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('Multado! Você excedeu o limite máximo de 80km/h.')
    print(f'Você deverá pagar uma multa de R${multa:.2f}')    
    print('Tenha um bom dia! Dirija com segurança')