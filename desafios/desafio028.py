# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu!

from random import randint
from time import sleep
numero = int(
    input("Tente adivinhar o número de 0 a 5 que o computador pensou: "))
print("Processando....")
sleep(1.5)

while True:
    sorteio = randint(0, 5)
    if numero == sorteio:
        print(
            f"Parabéns! Você digitou {numero} e a máquina também digitou {sorteio}, por tanto, você venceu!")
        break
    else:
        print(
            f"Você digitou {numero} e a máquina pensou em {sorteio}. Não foi dessa vez :( !!")
        numero = int(input("Digite ou número inteiro de 0 a 5: "))
