# Crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


resposta = 'Ss'
soma = 0
quantidade = 0
media = 0

maior_numero = 0
menor_numero = 0

while resposta in 'Ss':
    numero = int(input("Digite um número: "))
    soma = soma + numero
    quantidade = quantidade + 1
    if quantidade == 1:
        maior_numero = menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
    resposta = str(input("Quer continuar? [S/N]")).strip()[0]
media = soma / quantidade

print(f"Você digitou {quantidade} e a média foi {media}")
print(f"O maior valor foi {maior_numero} e o menor valor foi {menor_numero}")
