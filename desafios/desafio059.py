# Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep

numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))


opcoes = 0

while opcoes != 5:
    opcoes = int(input(
        "Qual operação deseja realizar? \n[1] Somar\n[2] Multiplicar\n[3] Maior valor digitador\n[4] Novos números\n[5] Sair do programa \n"))

    if opcoes == 1:
        soma = numero1 + numero2
        print(f"A soma dos valores {numero1} e {numero2} é igual a {soma}!")

    elif opcoes == 2:
        multiplicar = numero1 * numero2
        print(
            f"A multiplicação dos valores {numero1} e {numero2} é igual a {multiplicar}!")

    elif opcoes == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
            print(
                f"Entre {numero1} e {numero2} o maior valor digitado foi {maior}")

    elif opcoes == 4:
        numero1 = int(input("Digite um novo valor: "))
        numero2 = int(input("Digite outr novo valor:  "))
    elif opcoes == 5:
        print("Entendido. Você finalizou o programa!")

    else:
        print("Opção inválida. Tente novamente!")
    sleep(1)
