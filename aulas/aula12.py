nome = str(input('Qual seu nome? '))

if nome =='Carlos':
    print('Que lindo nome')
elif nome == 'Pedro' or nome=='Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Juliana Claudia Jessica Juliana':
    print('Que belo nome feminino')    
else:
    print('Que nome normal')    

print(f'Tenho um bom dia! {nome}')       