# Aplicando Técnicas de Listas em Python
# Identificando os Produtos mais vendidos

#https://web.dio.me/coding/aplicando-tecnicas-de-listas-em-python/algorithm/identificando-os-produtos-mais-vendidos?back=/track/engenharia-dados-python


def produto_mais_vendido(produtos):
    contagem = {}
    max_produto = None
    max_count = 0
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

        if contagem[produto] > max_count:
            max_count = contagem[produto]
            max_produto = produto
        else:
            pass
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()

    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    entrada_csv = entrada.split(",")

    # Remove espaçoes em branco extras nas strings
    produtos = []
    for i in entrada_csv:
        produtos.append(i.strip())

    return produtos


produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))