'''Cenário: chatbot RAG

Você está desenvolvendo um chatbot para uma instituição financeira. O sistema consultou um banco vetorial e retornou os seguintes documentos, cada um com uma pontuação de similaridade.

documentos = [
    {"texto": "Política de crédito", "score": 0.95},
    {"texto": "Manual de férias", "score": 0.45},
    {"texto": "Regras de financiamento", "score": 0.87},
    {"texto": "Política de viagens", "score": 0.62}
    
    Sua tarefa: implemente uma função chamada filtrar_documentos que receba essa lista e retorne somente os documentos cujo score seja maior ou igual a 0.8.

O resultado esperado é:

[
    {"texto": "Política de crédito", "score": 0.95},
    {"texto": "Regras de financiamento", "score": 0.87}
]

Regras da simulação
- Pode utilizar for, if, funções e recursos nativos do Python.
- Não utilize bibliotecas externas.
- Tente resolver sem consultar IA ou pesquisar a solução.
- Se não souber alguma coisa, explique até onde conseguiu chegar.'''

# Solução:


documentos = [
    {"texto": "Política de crédito", "score": 0.95},
    {"texto": "Manual de férias", "score": 0.45},
    {"texto": "Regras de financiamento", "score": 0.87},
    {"texto": "Política de viagens", "score": 0.62}
]


def filtrar_documentos(documentos):
    documentos_filtrados = []

    for documento in documentos:

        if documento["score"] >= 0.8:

            documentos_filtrados.append(documento)
    return documentos_filtrados
