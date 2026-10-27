# Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1,250,00, calcule um aumento de 10%.

# Para os infeiores ou iguais, o aumento é de 15%.

from time import sleep

print("Dia do aumento!!!!!!!!")
sleep(1)

salario = float(input("Digite o seu valor atual do seu salário! R$"))


if salario >= 1250:
    aumento1 = (salario * 10 / 100) + salario
    print(
        f"Seu salário de R${salario:.2f} teve um aumento de 10% e subiu para R${aumento1:.2f} ")
else:
    aumento2 = (salario * 15 / 100) + salario
    print(
        f"Seu salário de R${salario:.2f} teve um aumento de 15% e subiu para R${aumento2:.2f}")
