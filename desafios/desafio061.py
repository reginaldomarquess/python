# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=' * 10)
print("Gerador de PA")
print('-=' * 10)
primeito_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))

termo = primeito_termo
contador = 1

while contador <= 10:
    print(f"{termo} ->", end=' ')
    termo = termo + razao
    contador = contador + 1

print("FIM!!")
