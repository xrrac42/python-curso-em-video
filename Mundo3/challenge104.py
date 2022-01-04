
def leiaInt(msg):

    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mDigite um numero inteiro válido\033[m')
        if ok:
            break

    return valor    


n = leiaInt('Digte um numero')
print(f'Voce acabou de digitar o numero {n}')