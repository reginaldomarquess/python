# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar e quie no final mostre:

# A - Qual é o total gasto na compra
# B - Quantos produtos custam mais  de R$1000.00
# C - Qual é o nome do produto mais barato

print('-=' * 15)
print("Loja Virtual".center(30))
print('-='*15)

somatorio = 0
produtos1000 = 0
contador = 0
menor_preco = 0
mais_barato = ''
# abaixo eu pensei em algo a mais para deixar o programa um pouco mais próximo do mundo real
lista_caros = []

while True:
    nome_produto = str(input("Qual o nome do produto? "))
    valor_produto = float(input("Qual o valor do produto? R$"))

    contador = contador + 1
    somatorio = somatorio + valor_produto

    if valor_produto > 1000:
        produtos1000 = produtos1000 + 1
        # # Guardando os dados em um dicionário e adicionando-os à lista (criando uma lista de dicionários)
        produto_caro = {'nome': nome_produto, 'preco': valor_produto}
        lista_caros.append(produto_caro)

    if contador == 1:
        menor_preco = valor_produto
        mais_barato = nome_produto
    else:
        if valor_produto < menor_preco:
            menor_preco = valor_produto
            mais_barato = nome_produto
    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(
            input("Deseja continuar? [S/N]")).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*15)
print(f"O total da compra foi R${somatorio:.2f}")

if len(lista_caros) > 0:
    print("Lista com nome dos produtos acima de R$1000")
    for item in lista_caros:
        print(f" - {item['nome']} -> R${item['preco']:.2f}")
print(f"Total de {produtos1000} produto(s) custando mais de R$1000.00.")
print(
    f"O produto mais barato foi {mais_barato} que custa R$ {menor_preco:.2f}")
