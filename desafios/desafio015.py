# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
print("="*4 + "Checkout do Aluguel" + "="*4)
dias_alugados = (int(input("Por quantos dias o carro foi alugado? ")))

km_percorridos = (float(input("Por quantos quilômetros o carro percorreu? ")))

custo_por_dia = 60
custo_por_km = 0.15

custo_final_total = (dias_alugados * custo_por_dia) + \
    (km_percorridos * custo_por_km)

print(
    f"O Valor total a pagar pelos dias alugados e pelos Kms rodados é de R${custo_final_total:.2f}")
