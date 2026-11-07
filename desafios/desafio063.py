# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequieência de Fibonacci.

# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


print('-=' * 30)
print("Sequência de Fibonacci")
print('-=' * 30)

numero = int(input("Quantos termos você quer mostrar? "))

termmo1 = 0
termo2 = 1

print(f"{termmo1} -> {termo2}", end=' ')

contador = 3
while contador <= numero:
    termo3 = termmo1 + termo2
    print(f"-> {termo3}", end=' ')
    termmo1 = termo2
    termo2 = termo3
    contador = contador + 1
print("-> FIM!")
