# Faça um programa que leia o nome compelto de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza

# primeiro= Ana
# último= Souza

nome = str(input("Digite seu nome completo: ")).strip()


dividir = nome.split()

print(f"Seu primeiro nome é {dividir[0]}")
print(f"Seu último nome é {dividir[len(dividir)-1]}")
