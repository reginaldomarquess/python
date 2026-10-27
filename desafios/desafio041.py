# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date


nascimento = int(input("Digite o seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - nascimento

print(f"O atleta tem {idade} e está na categoria:")
if idade <= 9:
    print("MIRIM!")
elif idade <= 14:
    print("INFANTIL!")
elif idade <= 19:
    print("JÚNIOR!")
elif idade <= 25:
    print("SÊNIOR!")
else:
    print("MASTER!")
