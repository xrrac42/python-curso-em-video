while True:
    n = int(input("Quer saber a tabuada de qual numero?"))
    if n < 0:
        break
    print(f'TABUADA DO {n}')
    for x in range(1, 11):
        print(f'{n} x {x} = {n*x}')

   
