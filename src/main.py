from Item import Item
from Interface import Interface
from knapsack import solve_knapsack
from backtracking import find_selected_items 

def __main__():
    print("--- GERANDO ARTEFATOS ---")
    item_list = []
    # Cria 10 itens para popular a lista de artefatos
    for i in range(10):
        item_list.append(Item(Item.name_generator()))

    # Define a capacidade da mochila (Inventário)
    inventory_capacity = 10
    
    # Input do usuário para definição de classe e cálculo de poder
    choice = input("Escolha a classe do jogador (warrior, bandit, berserker, tank, (vazio)): ").strip().lower()
    
    # 1. Preparação dos dados: cálculo dos valores (poder) e separação em listas de weights e values
    for item in item_list:
        item.calculate_power(choice)

    weights = [item.size for item in item_list]
    values = [item.power for item in item_list]

    print(f"\nItens disponíveis: {len(item_list)}")
    print(f"Capacidade da Mochila: {inventory_capacity}")

    # 2. Execução do algoritmo da Mochila para obter o valor máximo e a tabela DP preenchida
    max_val, dp_table = solve_knapsack(inventory_capacity, weights, values)
    
    print(f"Valor Máximo Possível calculado: {max_val:.2f}")

    # 3. Recuperação dos itens selecionados utilizando a função de backtracking na tabela DP
    selected_items = find_selected_items(dp_table, inventory_capacity, weights, item_list)

    # Inicializa a interface para exibição dos resultados
    interface = Interface()

    print("\n--- TODOS OS ITENS DISPONÍVEIS ---")
    interface.show_multiple_items_details(item_list)
    
    # Exibe a build final com os itens selecionados pelo algoritmo
    interface.show_final_build(selected_items)

    # Validação dos totais de peso e valor para fins de verificação
    peso_total = sum([i.size for i in selected_items])
    valor_total = sum([i.power for i in selected_items])
    print(f"DEBUG: Peso Total: {peso_total}/{inventory_capacity} | Valor Total Real: {valor_total:.2f}")

if __name__ == "__main__":
    __main__()