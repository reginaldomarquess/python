# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500


somatorio = 0
cont = 0
for contador in range(1, 501, 2):
    # Lembrando que temos que verificar se o número é ímpar, por isso o % 2 != 0, que é se o resto da divisão por 2 é diferente de 0...
    if contador % 2 != 0 and contador % 3 == 0:
        cont = cont + 1
        somatorio = somatorio + contador
print(f"O somatório dos {cont} valores solicitados é igual a {somatorio}")
