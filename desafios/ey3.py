# Identificação de erros de API
# Imagine que você desenvolveu uma aplicação de IA que consome uma API de LLM. Após várias requisições, o sistema registrou as seguintes respostas:

respostas = [
    {"id": 1, "status": 203},
    {"id": 2, "status": 500},
    {"id": 3, "status": 200},
    {"id": 4, "status": 429},
    {"id": 5, "status": 303}
]

# Sua missão é criar uma função chamada identificar_erros que receba essa lista e retorne uma nova lista contendo apenas os dicionários cujo status seja maior ou igual a 400.

# Resultado esperado:

'''[
    {"id": 2, "status": 500},
    {"id": 4, "status": 429},
    {"id": 5, "status": 503}
]'''


def identtificar_erros(respostas):

    lista_respostas = []

    for resposta in respostas:
        if resposta["status"] >= 400:

            lista_respostas.append(resposta)
    return lista_respostas


resultado = identtificar_erros(respostas)

print(resultado)
