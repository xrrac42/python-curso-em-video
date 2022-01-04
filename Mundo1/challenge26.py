frase=str(input('Digite uma frase: ')).upper().strip()
contador= frase.count('A')
first= frase.find('A')+1
last = frase.rfind("A")+1

print(f'A letra aparece A  {contador} vezes')
print(f'A letra A apareceu pela primeira vez na posição {first}')
print(f'A letra A apareceu na última vez na posição {last}')