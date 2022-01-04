frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso= ''

for letra in range(len(juntar) -1,-1,-1):
    inverso += juntar[letra] 

if inverso == juntar:
    print('É palindromo')
else:
    print('Não é palindromo')    