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

        # poder do amuleto calculado com base nos atributos (multiplicadores provisorios)
        self.power = (self.life * 1.25) + (self.strength * 1.5) + (self.speed * 1.35) + (self.resistance * 1.2)

        #informações visuais para a representação do item pela interface
        self.sides = random.choice(["||", "//", "--", "\\"])
        self.simbol = random.choice(["🧠", "💎", "🎯", "🐉", "💣", "🔮", "🧪", "🧬", "🔥", "❄️", "⚡"])
    
    @staticmethod
    def name_generator() -> str:
        """
        Gera um nome aleatório para o item.
        """
        # Prefixos genericos de itens comuns em jogos RPG 
        prefix = ["Invólucro", "Casca", "Garra", "Perspicacia", "Escudo", "Sabedoria", "Fúria", "Brilho", "Anel", "Essência", "Sabor"]
        #Sufixos baseados em frutas para dar um tom comico e relacionado ao tema
        suffix = ["Melancia", "Jaca", "Uva", "Maça", "Abacaxi", "Manga", "Banana", "Limão", "Laranja", "Morango", "Pitaia", "Kiwi"]
        return f"{random.choice(prefix)} de {random.choice(suffix)}"
    
    def __str__(self) -> str:
        return f"Item({self.name}, Life: {self.life}, Strength: {self.strength}, Speed: {self.speed}, Resistance: {self.resistance}, Size: {self.size}, Power: {self.power:.2f})"