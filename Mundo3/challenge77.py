palavras = ('aprender', 'programar', 'linguagem', 'python',
'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')
