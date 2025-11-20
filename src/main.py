from Item import Item
from Interface import Interface
from knapsack import solve_knapsack

def __main__():
    lista_itens = []
    # Cria itens de exemplo com nomes gerados aleatoriamente
    for i in range(5):
        lista_itens.append(Item(Item.name_generator()))

    
    
    # Calcula o poder dos itens
    choice = input("Escolha a classe do jogador (warrior, bandit, berserker, tank, none): ").strip().lower()
    for item in lista_itens:
        item.calculate_power(choice)

    print(solve_knapsack(capacity=10, weight=[item.size for item in lista_itens], values=[item.power for item in lista_itens])[1])

    lista_itens_finais = [lista_itens[0], lista_itens[2], lista_itens[4]]

    # Inicializa a interface
    interface = Interface()

    # Mostra os detalhes do item
    interface.show_item_details(lista_itens[0])
    interface.show_multiple_items_details(lista_itens)
    interface.show_final_build(lista_itens_finais)

if __name__ == "__main__":
    __main__()