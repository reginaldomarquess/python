# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("Suas opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura")

jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
print('-=' * 11)

print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")

print('-=' * 11)

if computador == 0:  # Jogou pedra
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVÁLIDAs")
elif computador == 1:  # Jogou papel
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDAs")
elif computador == 2:  # Jogou tesoura
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDAs")
