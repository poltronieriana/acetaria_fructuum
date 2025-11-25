from tabulate import tabulate

class Interface:
    """
    Classe de interface para exibir informações dos itens.
    """

    def __init__(self):
        """
        Inicializa a interface.
        """
        pass

    def show_item_details(self, item):
        """
        Mostra os detalhes de um item especifico.
        """
        print("\n" + f"{item.sides}" * 40)
        print((item.name).center(len(item.sides) * 40))
        print(f"{item.sides}" * 19 + f"({item.simbol})" + f"{item.sides}" * 19)
        print(f" Vida: {item.life}")
        print(f" Força: {item.strength}")
        print(f" Velocidade: {item.speed}")
        print(f" Resistência: {item.resistance}")
        print(f" Tamanho: {item.size}")
        print(f" Poder: {item.power:.2f}")
        print("=" * 40 + "\n")

    def show_multiple_items_details(self, item_list):
        """
        Mostra os detalhes de uma lista de itens através de uma tabela.
        """
        table_data = []
        for item in item_list:
            table_data.append([item.name, item.life, item.strength, item.speed, item.resistance, item.size, f"{item.power:.2f}"])
        headers = ["Nome", "Vida", "Força", "Velocidade", "Resistência", "Tamanho", "Poder"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        input("\nPressione Enter para continuar...\n")  
    
    def show_final_build(self, item_list):
        """
        Mostra a build final do jogador com os itens equipados.
        """
        accumulated_power = 0
        print("\n" + "=" * 80)
        print("BUILD FINAL DO JOGADOR".center(80))
        print("=" * 80 + "\n")
        for item in item_list:
            print(f"--" * 40)
            print((item.name).center(80))
            print(f"--" * 19 + f"({item.simbol})" + f"--" * 19)
            accumulated_power += item.power
        print("\n" + "=" * 80)
        print("PODER ACUMULADO DOS ITENS EQUIPADOS".center(80))
        print(f"{accumulated_power:.2f}".center(80))
        print("=" * 80 + "\n")
       
    
    