# Crie um programa que leia um número inteiro e mostre na tela ele é PAR ou ÍMPAR.

numero = int(input("Digite um número inteiro qualquer: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é ÍMPAR!")
