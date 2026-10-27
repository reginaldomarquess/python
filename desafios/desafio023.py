# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos serparados.
# Ex: Digite um número: 1834

# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
from time import sleep
numero = int(input("Digite um número até 9999: "))
# (Divisão Inteira): Ele divide o número por 1 e descarta as casas decimais
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Analisando o número {numero}......")
sleep(1)
print(f"unidade: {unidade}")
print(f"dezena: {dezena}")
print(f"centena: {centena}")
print(f"milhar: {milhar}")
