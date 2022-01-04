expressao = []

expressao.append(input('Digite sua expressao: '))
abrindo = expressao.count('(')
fechando = expressao.count(')')

if abrindo == fechando:
    print('Expressão válida')
else:
    print('Expressão inválida')
