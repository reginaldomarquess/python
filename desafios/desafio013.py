# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_inicial = (float(input("Qual o salário atual do funcionário? R$")))

aumento = 0.15

salario_final = salario_inicial + (salario_inicial * aumento)


print(
    f"O funcionário que ganhava R${salario_inicial} teve 15% de aumento, e a gora passa a receber R${salario_final:.2f}")
