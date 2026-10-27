# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/chegue: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal, sem desconto ou acréssimo
# 3x ou mais no cartão: 20% de juros
print('=-='*10, "Let's go to EY", '=-='*10)


valor_produto = float(input("Informe o valor do produto: R$"))


opcoes_compra = int(input(
    "Qual a forma de pagamento?\n[1] À vista em dinheiro/chegue com 10%  desconto\n[2] À vista no cartão com 5% de desconto\n[3] 2x no cartão sem Juros\n[4] 3x no cartão com 20% de juros\n "))


if opcoes_compra == 1:
    desconto_10 = valor_produto - (valor_produto * 10 / 100)
    print(
        f"O produto de R${valor_produto:.2f} comprado à vista no dinheiro/cheque recebe um desconto de 10%, por tanto, você pagará R${desconto_10:.2f}.")

elif opcoes_compra == 2:
    desconto_5 = valor_produto - (valor_produto * 5 / 100)
    print(
        f"O produto de R${valor_produto:.2f} comprado à vista no cartão recebe 5% de desconto e, por tanto, você pagará R${desconto_5:.2f}")

elif opcoes_compra == 3:
    parcela = valor_produto / 2
    print(
        f"O produto de R${valor_produto:.2f} comprado em 2x no cartão não recebe desconto nem acréssimo em juros. Você pagará 2 parcelas de R${parcela:.2f}.")

elif opcoes_compra == 4:
    juros = valor_produto + (valor_produto * 20 / 100)
    total_parcelas = int(input("Quantas parcelas? "))
    parcelas = juros / total_parcelas
    print(
        f"O produto de R${valor_produto:.2f} comprado em {total_parcelas}x no cartão terá 20% de juros e, por tanto, você pagará {total_parcelas} parcelas de R${parcelas:.2f} totalizando em R${juros:.2f}.")
else:
    total = 0
    print("Opção inválida de pagamento. Tente novamente!")
