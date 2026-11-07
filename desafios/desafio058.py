# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer!


from random import randint
from time import sleep

numero = int(input("Tente adivinha o número que o computador pensou: "))

palpite = 0
computador = randint(0, 10)

while numero != computador:
    palpite = palpite + 1
    if numero != computador:
        numero = int(input("O computador venceu. Tente novamente: "))
print(
    f"Parabéns! Você venceu e precisou de {palpite} tentativas para vencer o computador!")


# Abaixo o método do professor:

computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.\nSerá que você consegeu adivinhar qual foi? ")

acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais uma vez.")
        elif jogador > computador:
            print("Menos, Tente mais uma vez.")

print(
    f"Parabéns! Você conseguiu acertar o número que o comptuador pensou depois de tentar {palpites} vezes!!")
