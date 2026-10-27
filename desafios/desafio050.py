# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

somatorio = 0
cont = 0
for contador in range(1, 7):
    numero = int(input(f"Digite o {contador}º valor inteiro qualquer: "))
    if numero % 2 == 0:
        somatorio = somatorio + numero
        cont = cont + 1

print(f"Você informou {cont} números pares e o somátorio foi {somatorio}")
