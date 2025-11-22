import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from backtracking import find_selected_items

class MockItem:
    """
    Classe auxiliar para simulação de objetos Item nos testes unitários.
    """
    def __init__(self, name, size, power):
        self.name = name
        self.size = size
        self.power = power
    def __repr__(self):
        return self.name

def generate_dp_table(capacity, weights, values):
    """
    Gera uma tabela de programação dinâmica válida para uso nos casos de teste.
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                take = values[i-1] + dp[i-1][w - weights[i-1]]
                dont_take = dp[i-1][w]
                dp[i][w] = max(take, dont_take)
            else:
                dp[i][w] = dp[i-1][w]
    return dp

class TestBacktracking(unittest.TestCase):
    
    def setUp(self):
        self.itens = [
            MockItem("Item A", 2, 3),
            MockItem("Item B", 3, 4),
            MockItem("Item C", 4, 5),
            MockItem("Item D", 5, 9),
        ]
        self.pesos = [i.size for i in self.itens]
        self.valores = [i.power for i in self.itens]

    def test_prioridade_valor(self):
        cap = 5
        dp = generate_dp_table(cap, self.pesos, self.valores)
        escolhidos = find_selected_items(dp, cap, self.pesos, self.itens)
        
        self.assertEqual(len(escolhidos), 1)
        self.assertEqual(escolhidos[0].name, "Item D")

    def test_preenchimento_exato(self):
        cap = 7
        dp = generate_dp_table(cap, self.pesos, self.valores)
        escolhidos = find_selected_items(dp, cap, self.pesos, self.itens)
        
        nomes = sorted([i.name for i in escolhidos])
        self.assertEqual(nomes, ['Item A', 'Item D'])

    def test_mochila_vazia(self):
        dp = generate_dp_table(0, self.pesos, self.valores)
        escolhidos = find_selected_items(dp, 0, self.pesos, self.itens)
        self.assertEqual(escolhidos, [])

if __name__ == '__main__':
    unittest.main()