from time import sleep
nome = str(input("Digite seu nome completo: ")).strip()
nospace= len(nome) - nome.count(" ")
separa = nome.split()

print("Analisando seu nome...")
sleep(0.5)
print(f"Seu nome em maiúsculo é {nome.upper()}")

print(f"Seu nome em minúsculo é {nome.lower()}")

print(f"Seu nome tem {nospace} letras" )

print(f"Seu primeiro nome é {separa[0].capitalize()} e tem {len(separa[0])} letras")
