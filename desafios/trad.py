from deep_translator import MyMemoryTranslator, GoogleTranslator

texto = input("Digite algo para traduzir: ")

try:
    traducao = GoogleTranslator(source='auto', target='pt').translate(texto)
except Exception:
    traducao = MyMemoryTranslator(
        source='en-US', target='pt-BR').translate(texto)

print(traducao)
