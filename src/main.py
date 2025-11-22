from Item import Item
from Interface import Interface
from knapsack import solve_knapsack
from backtracking import find_selected_items 

def __main__():
    print("--- GERANDO ARTEFATOS ---")
    lista_itens = []
    # Cria 10 itens para popular a lista de artefatos
    for i in range(10):
        lista_itens.append(Item(Item.name_generator()))

    # Define a capacidade da mochila (Inventário)
    CAPACIDADE_MOCHILA = 15
    
    # Input do usuário para definição de classe e cálculo de poder
    choice = input("Escolha a classe do jogador (warrior, bandit, berserker, tank, none): ").strip().lower()
    
    # 1. Preparação dos dados: cálculo dos valores (poder) e separação em listas de pesos e valores
    for item in lista_itens:
        item.calculate_power(choice)

    pesos = [item.size for item in lista_itens]
    valores = [item.power for item in lista_itens]

    print(f"\nItens disponíveis: {len(lista_itens)}")
    print(f"Capacidade da Mochila: {CAPACIDADE_MOCHILA}")

    # 2. Execução do algoritmo da Mochila para obter o valor máximo e a tabela DP preenchida
    max_val, dp_table = solve_knapsack(CAPACIDADE_MOCHILA, pesos, valores)
    
    print(f"Valor Máximo Possível calculado: {max_val:.2f}")

    # 3. Recuperação dos itens selecionados utilizando a função de backtracking na tabela DP
    itens_escolhidos = find_selected_items(dp_table, CAPACIDADE_MOCHILA, pesos, lista_itens)

    # Inicializa a interface para exibição dos resultados
    interface = Interface()

    print("\n--- TODOS OS ITENS DISPONÍVEIS ---")
    interface.show_multiple_items_details(lista_itens)
    
    # Exibe a build final com os itens selecionados pelo algoritmo
    interface.show_final_build(itens_escolhidos)

    # Validação dos totais de peso e valor para fins de verificação
    peso_total = sum([i.size for i in itens_escolhidos])
    valor_total = sum([i.power for i in itens_escolhidos])
    print(f"DEBUG: Peso Total: {peso_total}/{CAPACIDADE_MOCHILA} | Valor Total Real: {valor_total:.2f}")

if __name__ == "__main__":
    __main__()