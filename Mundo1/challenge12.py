price= float(input("Qual é o preço do produto? "))
off= price - (price*5/100)
print(f"O produto que custava R${price:.2f}, na promoção com desconto de 5% vai custar R${off:.2f}")