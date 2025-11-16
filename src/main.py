from Item import Item
from Interface import Interface

def __main__():
    # Cria itens de exemplo com nomes gerados aleatoriamente
    item_exemplo = Item(Item.name_generator())
    item_exemplo1 = Item(Item.name_generator())
    item_exemplo2 = Item(Item.name_generator())
    item_exemplo3 = Item(Item.name_generator())
    item_exemplo4 = Item(Item.name_generator())
    lista_itens = [item_exemplo, item_exemplo1, item_exemplo2, item_exemplo3, item_exemplo4]
    lista_itens_finais = [item_exemplo2, item_exemplo4]

    # Inicializa a interface
    interface = Interface()

    # Mostra os detalhes do item
    interface.show_item_details(item_exemplo)
    interface.show_multiple_items_details(lista_itens)
    interface.show_final_build(lista_itens_finais)

if __name__ == "__main__":
    __main__()