# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, sele ainda vali se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Digite o seu nao de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    tempo_faltante = 18 - idade
    ano_alistamento = ano_atual + tempo_faltante
    print(
        f"Você tem {idade} e não precisa se alistar ainda, pois faltam {tempo_faltante} anos(s) para o seu alistamento!\nSeu ano de alistamento será em {ano_alistamento}! ")
elif idade > 18:
    tempo_excedido = idade - 18
    ano_alistamento = ano_atual - tempo_excedido
    print(f"Você tem {idade} e já passou do tempo de se alistar {tempo_excedido} ano(s)!!!\nO seu alistamento era em {ano_alistamento}")
else:
    print(
        f"Você já tem {idade} anos de idade. ESSE É O SEU ANO DE ALISTAMENTO!!")
