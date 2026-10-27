# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco_inicial = (float(input("Qual o valor do produto? R$ ")))

desconto = 0.05

preco_final = preco_inicial - (preco_inicial * desconto)

print(
    f"O produto que valia R${preco_inicial} agora com 5% de desconto, vale R${preco_final:.2f}")
