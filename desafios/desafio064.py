# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números forma digitados e qual foi a soma entre eles (desconsiderando a flag 999).

print("-="*15)
print("Promgram V8".center(30))
print("-="*15)

numero = 0
contador = 0
soma = 0
numero = int(input("Digite um número [ou se preferir para digite 999]: "))
while numero != 999:
    contador = contador + 1
    soma = soma + numero
    numero = int(input("Digite um número [ou se preferir para digite 999]: "))
print(f"O somátior de todos os {contador} números digitados foi {soma}")
