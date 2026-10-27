# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.
# Considere a maioridade : 21 anos

from datetime import date

ano_atual = date.today().year
total_maior = 0
total_menor = 0

for pessoas in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {pessoas}ª pessoa nasceu? "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1
print(
    f"Ao todo tivemos {total_maior} pessoas maiores de idade e {total_menor} pessoas menores de idade!")
