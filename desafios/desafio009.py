# Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada.

numero = (int(input("Digite um número para ver a sua tabuada: ")))

tabuada = 0
# i é o iterador (aquilo que se repete), também poderíamos usar o nome de "contador" ou "variável de controle"
print("=" * 12)
for i in range(1, 11):
    tabuada = numero * i

    print(f"{numero} x {i:2} = {tabuada}")
print("=" * 12)
