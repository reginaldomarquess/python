# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5x4x3x2x1 = 120


numero = int(input("Digite um valor para saber o seu vatorial: "))

contador = numero
fatorial = 1
print(f"Clalculando {numero}!", end=' ')
while contador > 0:
    print(f"{contador}", end=' ')
    print(" x " if contador > 1 else '=', end=' ')
    fatorial = fatorial * contador
    contador = contador - 1
print(f"{fatorial}")
