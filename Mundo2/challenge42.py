s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))

if s1<s2+s3 and s2<s3+s1  and s3<s2+s1:
    condition = 'Podem formar um triângulo'
    if s1 == s2 == s3:
        classification ='Equilátero'
    elif s1 != s2 != s3:
        classification = 'Escaleno'
    else:
        classification = 'Isoceles'
else:
    condition = 'Nao podem formar um triangulo'
    classification =''        

print(f'Os segmentos acima {condition.upper()} {classification.upper()}')