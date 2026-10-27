# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado!

valor_casa = float(input("Qual o valor da casa? R$"))
salário = float(input("Qual o seu salário? R$"))
anos_pagando = int(input("Em quantos anos deseja pagar? "))

minimo = salário * 30 / 100

mensalidade = valor_casa / (anos_pagando * 12)
print(
    f"Para comprar uma casa de R${valor_casa:.2f} em {anos_pagando} ano(s) a mensalidade será de R${mensalidade:.2f}")

if mensalidade <= minimo:
    print(f"Empréstimo CONSEDIDO!!")

else:
    print("O valor da mensalidade excede 30% do seu salário. Empréstimo NEGADO!!")
