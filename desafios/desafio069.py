# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quantos homens foram cadastrados
# C - Quantas mulheres tem menos de 20 anos

print('-='*15)
print("Cadastro de Pessoas".center(30))
print('-='*15)


maiores18 = 0
homens = 0
mulheres_menor20 = 0

while True:
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Digite seu sexo [M/F]")).strip().upper()[0]

    if idade >= 18:
        maiores18 = maiores18 + 1

    if sexo == 'M':
        homens = homens + 1

    if sexo == 'F' and idade < 20:
        mulheres_menor20 = mulheres_menor20 + 1

    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if continuar == 'N':
        break
print(f"Total de {maiores18} pessoa(s) maiores de 18 anos cadastradas!\nTotal de {homens} homem(s) cadastrados!\nTotal de {mulheres_menor20} mulher(es) com menos de 20 anos cadastradas!")
