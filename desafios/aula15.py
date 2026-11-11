'''contador = 1

while contador <= 10:
    print(contador, ' -> ', end=' ')
    contador = contador + 1
print("Acabou!")'''

# contador = 0
numero = 0
soma = 0

while numero != 999:
    numero = int(input("Digite um número itneiro: "))
    if numero == 999:
        break
    soma = soma + numero

print(f"A soma foi {soma}")
