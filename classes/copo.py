# Desenvolva sua classe Copo aqui.
from .recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho: float):
        super().__init__(tamanho)

    def __str__(self):
        if self.conteudo == 0:
            return f"Um copo vazio de {self.tamanho}ml"

        return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"
      
    def __repr__(self):
        if self.conteudo == 0:
            return f"Um copo vazio de {self.tamanho}ml"

        return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

    def encher(self, bebida: str = 'água'):
        if not self.limpo:
            return 'Não se pode encher um copo sujo'
        
        self.bebida = str(bebida)
        self.limpo = bool(False)
        self.conteudo = float(self.tamanho)

    def beber(self, quantidade: float):
        if quantidade > self.conteudo:
            return 'Não há bebida suficiente no copo'
        if quantidade < 0:
            return 'Quantidade deve ser positiva'

        self.conteudo = self.conteudo - quantidade

    def lavar(self):
        self.bebida = None
        self.limpo = bool(True)
        self.conteudo = float(0)