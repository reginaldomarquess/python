# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

aluno1 = input("Digite o nome do primeiro aluno(a): ")
aluno2 = input("Digite o nome do segundo aluno(a): ")
aluno3 = input("Digite o nome do terceiro aluno(a): ")
aluno4 = input("Digite o nome do quarto aluno(a): ")

alunos = [aluno1, aluno2, aluno3, aluno4]

aluno_sorteado = choice(alunos)

print(f"O aluno(a) sorteado para apagar o quadro foi o {aluno_sorteado}.")
