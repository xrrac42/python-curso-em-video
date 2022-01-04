nome = input('Digite o nome: ')
gols = input('Digite os gols marcados')
def ficha(nome,gols):
 if gols.isnumeric():
   gols = int(gols)
 else:
  gols = 0 

 if nome.strip == '':
   ficha(gols=gols)
 else:
   ficha(nome,gols)

ficha(nome,gols)   