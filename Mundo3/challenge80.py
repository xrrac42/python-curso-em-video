valores = []

for x in range(0, 5):
    valor= int(input(f'Digite o valor da posicao {x} '))
    if x == 0 or x > valores[-1]:
        print('Adicionado ao inicio da lista')
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
                if valor <= valores[pos]:
                    valores.insert(pos,valor)
                    print(f'Adicionado na posicao {pos}')
                    break
                pos += 1

print(valores)