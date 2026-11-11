# Crie um programa que leia vários números inteiros pelo teclado.  programa só vai parar quando o usuário digitar o valor 999, que é a condião de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag.)


soma = 0
contador = 0
# laço infinito
while True:
    numero = int(
        input("Digite um número [ou digite 999 para sair do programa]: "))
    # minha condição de parada
    if numero == 999:
        break
    # somatório
    soma = soma + numero
    # contador propriamente dito
    contador = contador + 1
print(f"A soma de todos os {contador} números digitados é {soma}.")
