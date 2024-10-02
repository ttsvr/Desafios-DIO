def analise_vendas(vendas, total_vendas = 0):
    # TODO: Calcule o total de vendas e realize a média mensal:
    
    # Total de vendas
    for i in vendas:
      total_vendas = total_vendas + i
      
    #Média mensal
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    
    #Divide os elementos da entrada do usuário por vírgula
    entrada_csv = entrada.split(",")
    
    # TODO: Converta a entrada em uma lista de inteiros:
    entrada_csv_int = map(int, entrada_csv)
    vendas = list(entrada_csv_int)
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))