# Ecreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input("Digite um número inteiro qualquer: "))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

escolha = int(input(
    f"Escolha uma das opções para converter o número digitado em outras bases!\n[1] BINÁRIO \n[2] OCTAL\n[3] HEXADECIMAL"))


if escolha == 1:
    print(f"O número {numero} covertido para BINÁRIO é {binario[2:]}.")
elif escolha == 2:
    print(f"O número {numero} convetido para OCTAL é {octal[2:]}.")
else:
    print(
        f"O numero {numero} convertido para HEXADECIMAL é {hexadecimal[2:]}.")
