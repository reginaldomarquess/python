# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = int(input("Digite um número: "))

total_divisivel = 0

for cont in range(1, numero + 1):
    if numero % cont == 0:
        print("\033[33m", end=' ')
        total_divisivel = total_divisivel + 1
    else:
        print("\33[31m", end=' ')
    print(f"{cont}", end=' ')
print(f"\nO número {numero} foi divisível {total_divisivel} vezes")
if total_divisivel == 2:
    print("E por isso ele é um número PRIMO!")
else:
    print("E por isso ele NÃO É UM NÚMERO PRIMO!!")
