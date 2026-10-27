# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


from math import sin, cos, tan, radians

angulo = float(input("Digite um ângulo: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(
    f"O ângulo de {angulo}º tem o Seno de {seno:.2f} o Cosseno de {cosseno:.2f} e a Tangente {tangente:.2f}")
