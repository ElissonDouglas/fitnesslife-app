import requests
from googletrans import Translator


def frase_motivacional() -> str:
    tradutor = Translator()

    leitor = requests.get(url='https://zenquotes.io/api/random')

    texto = leitor.json()
    autor = texto[0]['a']
    frase = tradutor.translate(texto[0]['q'], dest='pt').text
    frase_saida = f"'{frase}' - {autor}"
    return  frase_saida
