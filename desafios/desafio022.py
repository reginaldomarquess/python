# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todos as letras maiúsculas

# O nome com todas minúsculas

# Quantas letras ao todo (sem considerara espaços)

# Quantas letras tem o primeiro nome


nome = str(input("Digite o seu nome completo: ")).strip()

primeiro_nome = nome.split()
sem_espacos = "".join(nome.split())
print(nome.upper())
print(nome.lower())
print(len(sem_espacos))
print(len(primeiro_nome[0]))
