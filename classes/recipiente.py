# Desenvolva sua classe Recipiente aqui.
class Recipiente():
    def __init__(self, tamanho: float):
        if tamanho < 0:
            tamanho = 0
        
        self.tamanho = float(tamanho)
        self.conteudo = float(0)
        self.limpo = bool(True)

    def __str__(self):
        return f"Um recipiente {self.estado()} não especificado"
      
    def __repr__(self):
        return f"Um recipiente {self.estado()} não especificado"

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if self.conteudo == 0:
            return True

        return False

    def lavar(self):
        self.limpo = bool(True)
        self.conteudo = 0

    def esta_limpo(self):
        return self.limpo

    def estado(self):
        if self.limpo:
            return "limpo"
        else:
            return "sujo"

    def sujar(self):
        self.limpo = bool(False)