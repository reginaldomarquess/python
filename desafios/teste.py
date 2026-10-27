'''inicio = int(input("Digite um número: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite os passos: "))

for contador in range(inicio, fim+1, passo):
    print(contador)
print("FIM!")'''


# somatório com for

somatorio = 0
for contador in range(0, 4):
    numero = int(input("Digite um valor inteiro: "))
    somatorio = somatorio + numero
print(f"O somatório de todos os números é {somatorio}")
