documentos = [
    {"texto": "Política de crédito", "score": 0.95},
    {"texto": "Manual de férias", "score": 0.45},
    {"texto": "Regras de financiamento", "score": 0.87},
    {"texto": "Política de viagens", "score": 0.62},
    {"texto": "Normas bancárias", "score": 0.91}
]
# Sua m
# issão: crie uma função chamada contar_documentos_relevantes que receba a lista de documentos e retorne quantos possuem score maior ou igual a 0.8.


def documentos_relevantes(documentos):

    contador = 0

    for documento in documentos:

        if documento["score"] >= 0.8:
            contador = contador + 1

    return contador


resultado = documentos_relevantes(documentos)
print(resultado)
