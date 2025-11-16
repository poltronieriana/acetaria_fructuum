import random

class Item: 
    def _init_(self, nome: str) -> None:

        self.nome = nome

        #atributos do item com valores aleatórios entre 1 e 10
        self.vida = random.randint(1, 10)
        self.forca = random.randint(1, 10)
        self.velocidade = random.randint(1, 10)
        self.resistencia = random.randint(1, 10)
        self.espaco = random.randint(1, 10)

        #informações visuais para a representação do item
        self.laterais = random.choice(["||", "//", "-", "\\"])
        self.simbolo = random.choice(["%", "$", "#", "@", "&"])

    #metodo para calcular o poder do item baseado em seus atributos (com valores provisorios)
    def calcular_poder(self) -> int:
        poder = (self.vida * 1.25) + (self.forca * 1.5) + (self.velocidade * 1.35) + (self.resistencia * 1.2)
        return poder
   
    """   
    def repr(self) -> str:
        return f
    """