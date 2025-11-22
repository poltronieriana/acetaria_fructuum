def find_selected_items(dp, capacity, weights, artifacts):
    """
    Recupera os itens escolhidos percorrendo a tabela DP inversamente.
    """
    selected_items = []
    n = len(artifacts)
    w = capacity 
    
    # Itera do último item até o primeiro
    for i in range(n, 0, -1):
        
        # Se o valor difere da linha anterior, o item foi selecionado
        if dp[i][w] != dp[i-1][w]:
            # Ajuste de índice (DP base-1 vs Lista base-0)
            item_escolhido = artifacts[i-1]
            selected_items.append(item_escolhido)
            
            # Deduz o peso do item para buscar o restante na linha anterior
            w -= weights[i-1]
            
    return selected_items