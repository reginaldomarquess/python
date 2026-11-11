# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final.
from random import randint
from time import sleep
vitorias = 0


while True:
    print("-="*15)
    print("Jogo do ÍMPAR/PAR".center(30))
    print("-="*15)
    computador = randint(0, 11)
    jogada = str(input("Qual a sua escolha? ÍMPAR[I] ou PAR[P]? ")).upper()[0]

    jogador = int(input("jogue um número: "))
    print("Do")
    sleep(0.3)
    print("La")
    sleep(0.3)
    print("Si")
    sleep(0.3)
    print("Já")
    if jogada == 'P':
        if (jogador + computador) % 2 == 0:
            print(
                f"Você jogou {jogador} e o computador jogou {computador}.O jodador venceu!")
            vitorias = vitorias + 1
        else:
            print(
                f"Você jogou {jogador} e o computador jogou {computador}.Você perdeu!")
            break
    elif jogada == 'I':
        if (jogador + computador) % 2 != 0:
            print(
                f"Você jogou {jogador} e o computador jogou {computador}.Jogador venceu!")
            vitorias = vitorias + 1
        else:
            print(
                f"Você jogou {jogador} e o computador jogou {computador}.Jogador perdeu!")
            break
print('-='*15)
print(
    f"Game Over! Você conseguiu vencer um total de {vitorias} vez(ez) seguida(s).")
