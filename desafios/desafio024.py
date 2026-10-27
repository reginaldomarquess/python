# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input("Digite o nome da Cidade: ")).lower()

contem = cidade.split()

tem_santo = "santo" in contem[0]

if tem_santo == True:
    print("A cidade digitada começa com Santo")
else:
    print("A cidade digitada não começa com Santo")
