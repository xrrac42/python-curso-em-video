import math

angule = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angule))
cos = math.cos(math.radians(angule))
tan = math.tan(math.radians(angule))

print(f"O ângulo de {angule} tem SENO de {seno:.2f}")
print(f"O ângulo de {angule} tem COSSENO de {cos:.2f}")
print(f"O ângulo de {angule} tem TANGENTE de {tan:.2f}")