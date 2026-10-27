# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input("Digite o seu nome completo: ")).strip()

tem_silva = "silva" in nome

if tem_silva == True:
    print(f"O nome {nome.lower()} contém Silva!")
else:
    print(f"O nome {nome.lower()} não contém Silva")
