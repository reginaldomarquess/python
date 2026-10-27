# Faça um programa que leia uma frase pelo teclado e mostre:

# Quentas vezes aparece a letra "a".
# Em que posilção ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase qualquer: ")).strip()

contador = frase.lower().count("a")


encontrar_inicio = frase.lower().find("a")+1

encontrar = frase.lower().rfind("a")+1
print(f"A letra 'a' aparece {contador} vezes na frase")

print(f"A letra 'a' aparece a primeira vez na poisção {encontrar_inicio}")

print(f"A letra 'a' aparece a última vez na posição {encontrar}")
