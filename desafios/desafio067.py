# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


tabuada = 0

while True:
    print('-=' * 20)
    numero = int(input(
        "Digite um número para ver a sua tabuada [digite qualquer número negativo para encerrar]: "))
    print('-=' * 20)
    if numero < 0:
        break
    for contador in range(1, 11):
        tabuada = numero * contador
        print(f"{numero} x {contador:2} = {tabuada} ")
