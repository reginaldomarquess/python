# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

'''numero = int(input("Digite um valor inteiro: "))
final = int(input("Digite o final da contagem: "))
passo = int(input("Digite os passos a serem contados: "))

for contador in range(numero, final, passo):
    print(f"Os números pares são: {contador}")
print('FIM!')'''

from time import sleep

for contador in range(2, 51, 2):
    print(f"Os números pares de 1 a 50 são: {contador}")
    sleep(0.3)
print("FIM!!!")
