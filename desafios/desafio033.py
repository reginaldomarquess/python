# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input("Digite um número inteiro qualquer: "))
numero2 = int(input("Digite um número inteiro qualquer: "))
numero3 = int(input("Digite um número inteiro qualquer: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} foi o maior número digitado!")

if numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} foi o maior número digitado!")

if numero3 > numero1 and numero3 > numero2:
    print(f"O número {numero3} foi o maior número digitado!")

if numero1 < numero2 and numero1 < numero3:
    print(f"O número {numero1} foi o menor número digitado!")

if numero2 < numero1 and numero2 < numero3:
    print(f"O número {numero2} foi o menor número digitado!")

if numero3 < numero2 and numero3 < numero1:
    print(f"O número {numero3} foi o menor número digitado!")
