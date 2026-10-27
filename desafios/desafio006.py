# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = (float(input("Digite um número: ")))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(
    f"O dobro do número {numero} é \033[0;31;41m{dobro}\033[m, \nO triplo de {numero} é \033[0;31;41m{triplo}\033[m \nE a raiz quadrada é \033[0;31;41m{raiz_quadrada:.2f}\033[m!")
