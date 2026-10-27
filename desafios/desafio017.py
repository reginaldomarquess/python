# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''from math import sqrt

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

soma_quadrados = (cateto_oposto ** 2) + (cateto_adjacente ** 2)

hipotenusa = sqrt(soma_quadrados)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")'''

from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")
