# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

from time import sleep
print('=='*9)
print("Calculadora de IMC")
print('=='*9)
sleep(1)

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.1f}")

if imc < 18.5:
    print("Abaixo do Peso!")
elif imc <= 25:
    print("Peso ideal!")
elif imc < 30:
    print("Sobrepeso!")
elif imc <= 40:
    print("Obesidade!")
else:
    print("Obesidade mórbida!")
