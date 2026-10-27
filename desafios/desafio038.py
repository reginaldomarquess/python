# Escreve um programa que leia dois número inteiro e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1 = int(input("Digite um número inteiro qualuqer: "))
numero2 = int(input("Digite outro número inteiro qualquer: "))


if numero1 > numero2:
    print(f"O primeiro número digitado é o maior!")

elif numero2 > numero1:
    print(f"O segundo número digitador é o maior!")

else:
    print("Não existe valor maior, os dois são iguais!")
