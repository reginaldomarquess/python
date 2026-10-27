# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


'''from time import sleep

inicio = int(input("Inicie a contagem: "))
final = int(input("Final da contagem: "))
passo = int(input("Passos da contagem: "))

for contador in range(inicio, final, - 1, -passo):
    print(contador)
    sleep(1)
print("BOOMMMMMM!!")'''


from time import sleep

inicio = int(input("Inicie a contagem (ex: 10): "))
final = int(input("Final da contagem (ex: 0): "))
passo = int(input("Passos da contagem (ex: 1): "))

# O passo é multiplicado por -1 para andar para trás
# O final recebe -1 porque o range não inclui o número final
for contador in range(inicio, final - 1, -passo):
    print(contador)
    sleep(1)

print("BOOMMMMMM!!🎇🎆")
