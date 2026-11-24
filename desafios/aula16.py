# Alguns exemplos:

# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f"Eu vou comer {comida}")

for contador in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[contador]} na posição {contador}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("Eita! Comi pra caramba!")
# print(lanche[-2:])

# Podemos, também, utilizar o método SORTED (classificado/organizado)
print(sorted(lanche))

# Mais exemplos abaixo:
a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b

print(c)
print(len(c))
# Quantas vezes está aparecendo o número 5 dentro de c
print(c.count(5))
print(c.count(4))
print(c.count(9))
# Index do "valor" desejado
print(c.index(5))
# Procurando quantas vezes aparece o número 5 a partir da posição 1 -> isso é o que chamamos de deslocamento!
print(c.index(5, 1))

pessoa = ('Gustavo', 39, 'M', 99.88)
# De fato tuplas são imutáveis, mas podemos podemos apagar tuplas. Lembrando que não é possível apagar um item específico de uma tupla, apenas ela inteira
del (pessoa)
print(pessoa)
