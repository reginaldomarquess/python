# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127. O número de 6.127 tem a parte inteira 6.
from math import floor
# Eu usei o floor mas também poderia ter usado o trunc, mas o floor arredonda para baixo e o trunc apenas corta a parte decimal.
numero = float(input("Digite um número inteiro: "))
inteiro = floor(numero)

print(f"O número {numero} tem a parte inteira {inteiro}.")
