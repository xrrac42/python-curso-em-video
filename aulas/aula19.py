pessoas = {'nome': "Gustavo", 'sexo': 'M', 'idade': 22}
#print(f"O {pessoas['nome'] } tem idade de {pessoas['idade']} anos ")
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k in pessoas.keys():
#  print(k)
#for k in pessoas.values():
#  print(k)
#del pessoas['sexo']
#pessoas['nome'] = 'Leandro'
#pessoas['peso'] = 98.5
#for k, i in pessoas.items():
#  print(f'{k} = {i}')
#brasil = []
#estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'Sao Paulo', 'sigla':'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil)
#print(brasil[0]['sigla'])
#print(brasil[1]['uf'])
estado = dict()
brasil = list()
for c in range(0, 3):
  estado['UF'] = input('Unidade Federativa: ')
  estado['Sigla'] = input('A sigla do estado')
  brasil.append(estado.copy())

for e in brasil:
  for  v in e.values():
    print(v,end=' ')
  print()  