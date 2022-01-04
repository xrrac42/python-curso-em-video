from time import sleep

num = int(input('Qual numero voce quer saber a tabuada? '))

print('|￣￣￣￣￣￣￣￣￣￣￣￣￣￣|')
print(f'     TABUADA DO {num}')
print('|＿＿＿＿＿＿＿＿＿＿＿＿＿＿|')
print('')
for c in range(1,11):
    print(f'{num} x {c} = {num*c}')
    sleep(0.5)
