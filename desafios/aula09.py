

frase = "Curso em Vídeo Python"
# Ele vai do 9 ao 21, pulando de 2 em 2
# frase[9:21:2]

# Ele começa do início e vai até o 5, pegando os 5 primeiros caracteres
# frase[:5]

# Ele pegou do décimo quinto caractere em diante
# frase[15:]

# Ele vai pegar do nove em diante pulando de 3 em 3
frase[9::3]

print(frase[1:15])
print(frase.upper().count('O'))
print('Curso' in frase)
