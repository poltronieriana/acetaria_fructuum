import random

class Item: 
    """
    Classe que representa um item com atributos aleatórios.
    """
    def __init__(self, name: str) -> None:

        self.name = name

        # atributos do item com valores aleatórios entre 1 e 10
        self.life = random.randint(1, 10)
        self.strength = random.randint(1, 10)
        self.speed = random.randint(1, 10)
        self.resistance = random.randint(1, 10)

        # 1 e 5 para size em consideração ao tamanho do inventario
        self.size = random.randint(1, 5)

        # poder do amuleto que vai ser calculado com base nos atributos em um metodo separado
        self.power = 0

        #informações visuais para a representação do item pela interface
        self.sides = random.choice(["||", "//", "--", "\\"])
        self.simbol = random.choice(["🧠", "💎", "🎯", "🐉", "💣", "🔮", "🧪", "🧬", "🔥", "❄️", "⚡"])
    
    def calculate_power(self, type) -> float:
        """
        Calcula o poder do item com base em seus atributos e a classe escolhida pelo jogador.
        """
        # Guerreiro foca em força e vida, uma opção equilibrada 
        if type == "warrior":
            self.power = (self.life * 1.5) + (self.strength * 1.75) + (self.speed * 1.1) + (self.resistance * 1.3)
        # Bandido foca em velocidade e agilidade
        elif type == "bandit":
            self.power = (self.life * 1.2) + (self.strength * 1.1) + (self.speed * 1.8) + (self.resistance * 1.1)
        # Berserker foca em força bruta
        elif type == "berserker":
            self.power = (self.life * 1.5) + (self.strength * 2.0) + (self.speed * 1.0) + (self.resistance * 1.2)
        # Tank foca em resistência e vida, uma opção defensiva
        elif type == "tank":
            self.power = (self.life * 1.8) + (self.strength * 1.4) + (self.speed * 1.0) + (self.resistance * 1.8)
        # Se caso nenhuma classe for escolhida, o poder é calculado sem modificadores
        else:
            self.power = (self.life) + (self.strength) + (self.speed) + (self.resistance)
    
    @staticmethod
    def name_generator() -> str:
        """
        Gera um nome aleatório para o item.
        """
        # Prefixos genericos de itens comuns em jogos RPG 
        prefix = ["Invólucro", "Casca", "Garra", "Perspicacia", "Escudo", "Sabedoria", "Fúria", "Brilho", "Anel", "Essência", "Sabor"]
        #Sufixos baseados em frutas para dar um tom comico e relacionado ao tema
        suffix = ["Melancia", "Jaca", "Uva", "Maça", "Abacaxi", "Manga", "Banana", "Limão", "Laranja", "Morango", "Pitaia", "Kiwi", "Mamão", "Pêra"]
        return f"{random.choice(prefix)} de {random.choice(suffix)}"
    
    def __str__(self) -> str:
        return f"Item({self.name}, Life: {self.life}, Strength: {self.strength}, Speed: {self.speed}, Resistance: {self.resistance}, Size: {self.size}, Power: {self.power:.2f})"