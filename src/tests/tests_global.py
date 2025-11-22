import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Item import Item
from knapsack import solve_knapsack
from backtracking import find_selected_items

class TestSystemIntegration(unittest.TestCase):
    """
    Testes de integração para validar o fluxo completo de dados.
    """

    def test_fluxo_completo_consistencia(self):
        itens = [Item(f"Teste {i}") for i in range(5)]
        
        # Definição manual de atributos
        dados_teste = [
            (1, 10),  # Item 0
            (5, 100), # Item 1
            (3, 50),  # Item 2
            (2, 15),  # Item 3
            (4, 40)   # Item 4
        ]
        
        for i, (size, power) in enumerate(dados_teste):
            itens[i].size = size
            itens[i].power = power

        capacidade = 6
        pesos = [i.size for i in itens]
        valores = [i.power for i in itens]

        # Execução do algoritmo de programação dinâmica
        valor_maximo, dp_table = solve_knapsack(capacidade, pesos, valores)

        # Execução da função de recuperação dos itens selecionados
        itens_selecionados = find_selected_items(dp_table, capacidade, pesos, itens)

        # Validação A: Consistência do Valor Total
        soma_valor_reconstruido = sum(i.power for i in itens_selecionados)
        self.assertEqual(soma_valor_reconstruido, valor_maximo, 
                         "Falha de integridade: Valor recuperado diverge do valor calculado.")

        # Validação B: Respeito à Capacidade
        soma_peso_reconstruido = sum(i.size for i in itens_selecionados)
        self.assertLessEqual(soma_peso_reconstruido, capacidade, 
                             "Falha de restrição: Itens selecionados excedem a capacidade.")

        # Validação C: Verificação de Otimidade
        self.assertEqual(valor_maximo, 110)
        self.assertEqual(len(itens_selecionados), 2)
        
        print(f"\nTeste de Integração Concluído.")
        print(f"Valor Calculado (DP): {valor_maximo}")
        print(f"Valor Recuperado (Backtracking): {soma_valor_reconstruido}")

if __name__ == '__main__':
    unittest.main()