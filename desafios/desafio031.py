# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

'''km_viagem = int(input("Quantos Km terão essa viagem? "))


preco1 = 0.50 * km_viagem
preco2 = 0.45 * km_viagem

if km_viagem <= 200:
    print(
        f"Para uma viagem de {km_viagem}Km o valor cobrado será de R${preco1:.2f}!")
else:
    print(
        f"Para uma viagem de {km_viagem}Km o valor cobrado será de R${preco2:.2f}")'''

# Uma forma mais otimizada de fazer

km_viagem = int(input("Quantos Km terão essa viagem? "))

if km_viagem <= 200:
    preco = 0.50 * km_viagem
else:
    preco = 0.45 * km_viagem

print(
    f"Para uma viagem de {km_viagem}Km, o valor cobrado será de R${preco:.2f}!")
