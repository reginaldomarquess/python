# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto!


sexo = ""

while sexo != 'M' and sexo != 'F':
    # Fatiamos para pegar apenas a primeira letra. Se usuário digitar Masdulo, o programa vai pegar o M e o mesmo para Feminino
    sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()[0]

    if sexo != 'Mm' and sexo != 'Ff':
        print("Dados inválidos. Por favor, digite o sexo: ")
print("Dados salvos com sucesso!!")

'''abaixo a solução do professor:

sexo = str(input("Digite o seu sexo [M/F] "))

while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, informe o seu sexo:")).stripp().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.)
    '''
