# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
from datetime import date

ano_atual = date.today().year

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0


for pessoas in range(1, 5):
    print(f"----Nome da {pessoas}ª pessoa------ ")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).upper().strip()
    soma_idade = soma_idade + idade
    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 = total_mulher_20 + 1
media_idade = soma_idade / 4
print(f"A média de idade do grupo é de {media_idade}")
print(
    f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}")
print(f"Ao todo são {total_mulher_20} mulher(es) com menos de 20 anos.")
