# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = input("Digite o nome do primeiro aluno(a)")
aluno2 = input("Digite o nome do segundo aluno(a)")
aluno3 = input("Digite o nome do terceiro aluno(a)")
aluno4 = input("Digite o nome do quarto aluno(a)")


alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = shuffle(alunos)

print(f"A ordem para apresentar os trabalho será: {alunos}")
