# Melhores o desafio 061, perguntando para o usuário se el quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.


print('-=' * 10)
print("Gerador de PA")
print('-=' * 10)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} ->", end=' ')
        termo = termo + razao
        contador = contador + 1

    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM!")
