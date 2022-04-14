from collections import Counter


def analisa_frequencia_de_letras(texto, quantidade_letras_mais_comuns):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(quantidade_letras_mais_comuns)
    soma = 0
    proporcao: int
    for caractere, proporcao in mais_comuns:
        print("'{}' => {:.2f}%".format(caractere, proporcao * 100))
        soma += proporcao
    print("Porcentagem dos {} caracteres mais comuns no arquivo: {:.2f}%"
          .format(quantidade_letras_mais_comuns, (soma * 100)))


caminho = "texto.txt"
quantidade_letras_mais_comuns = 10

with open(caminho, "r") as arquivo:
    texto = arquivo.read().replace('\n', '')

analisa_frequencia_de_letras(texto, quantidade_letras_mais_comuns)
