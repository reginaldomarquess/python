# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite


velocidade = int(input("Qual foi a velocidade do veículo? "))

if velocidade > 80:
    velo_acima = velocidade - 80
    multa = (velocidade - 80) * 7
    print(
        f"Por estar a uma velocidade de {velocidade}Km/h você ultrapassou {velo_acima}Km/h acima do limite permitido e terá de pagar uma mulda de R${multa:.2f}")
else:
    print(
        f"A velocidade registrada foi de {velocidade}Km/h. Seu veículo estava dentro do limite permitido!")
