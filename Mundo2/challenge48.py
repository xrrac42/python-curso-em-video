soma = 0
count = 0
for x in range(1,501,2):
    if x %3 == 0:
        count += 1
        soma += x

print(f"A soma de todos {count} os valores solicitados é {soma}")        
      

