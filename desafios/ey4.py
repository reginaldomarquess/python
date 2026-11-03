# Desafio 4

# Imagine que você está desenvolvendo um sistema RAG para um banco. Após consultar um modelo de linguagem, sua aplicação recebe as seguintes respostas:

respostas_llm = [
    {"pergunta": "O que é crédito?", "resposta": "Crédito é um recurso financeiro."},
    {"pergunta": "Qual é a taxa?", "resposta": ""},
    {"pergunta": "Como solicitar empréstimo?",
        "resposta": "A solicitação pode ser feita pelo aplicativo."},
    {"pergunta": "Qual é o limite?", "resposta": ""}
]

'''Sua missão: implemente uma função chamada filtrar_respostas_validas que receba essa lista e retorne apenas os dicionários cuja chave "resposta" contenha uma string não vazia.

Resultado esperado:
[
    {
        "pergunta": "O que é crédito?",
        "resposta": "Crédito é um recurso financeiro."
    },
    {
        "pergunta": "Como solicitar empréstimo?",
        "resposta": "A solicitação pode ser feita pelo aplicativo."
    }
]
'''


def filtrar_respostas(lista_respostas):
    respostas_validas = []

    for resposta in lista_respostas:
        if resposta["resposta"] != "":
            respostas_validas.append(resposta)
    return respostas_validas


resultado = filtrar_respostas(respostas_llm)

print(resultado)
