# num = [2,5,9,1]
# num[2]= 11
# num.append(7)
# num.sort(reverse= True )
# num.insert(2,4)
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não temos o numero 4')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for cont in range(0,5):
#     valores.append(int(input('Digite os valores')))

# for c, v in enumerate(valores):
#     print(f'Na posicao {c} encontrei os valores {v}')

a = [1,2,3,4,5]
b = a[:]
b[2] = 8

print(f'Lista A {a}')
print(f'Lista B {b}')