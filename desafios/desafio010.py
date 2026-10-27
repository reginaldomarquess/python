# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostreo quantos dólares ela pode comprar.
# Considere US$1.00 = R$5.02

dinheiro = (float(input("Quanto você tem na carteira do nubank? R$ ")))

cotacao_dolar = 5.02

quanto_pode_comprar = dinheiro / cotacao_dolar

print(
    f"Com R${dinheiro:.2f} você pode comprar US${quanto_pode_comprar:.2f} em dólares.")
