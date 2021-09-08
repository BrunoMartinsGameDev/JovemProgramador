class Player:
    def __init__(self,nome,ponto = 0,rodada = 1,sePerdeu = False):
        self.nome = nome
        self.ponto = ponto
        self.rodada = rodada
        self.sePerdeu = sePerdeu
    def setPoint(self,newPoint):
        self.ponto = newPoint
    def getPoint(self):
        return self.ponto
    def getSePerdeu(self):
        return self.sePerdeu
    
    
