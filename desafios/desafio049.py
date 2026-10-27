# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


numero = int(input("Digite número para saber a sua tabuada: "))
print(f"A tabuada do número {numero} é: ")
for contador in range(1, 11):
    tabuada = contador * numero
    # coloquei o :2 para ele pular 2 casas da string e deixar a tabuada alinhada
    print(f"{numero} X {contador:2} = {tabuada}")
# print(f"A tabuada do número {numero} é {tabuada}")
