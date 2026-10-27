# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

somatorio = 0
for contador in range(0, 6):
    numero = int(input("Digite um valor inteiro qualquer: "))
    if numero % 2 == 0:
        somatorio = somatorio + numero

print(somatorio)
